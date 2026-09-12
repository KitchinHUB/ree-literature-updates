"""The controlled vocabulary the bibliography is faceted on.

Kept apart from `build_facets.py` so the vocabulary can be read, reviewed and
argued with on its own. It extends the index vocabulary in `tag_index.py` --
same terms where they overlap, same spelling -- because a reader who finds
"Cyanex 272" in the index should find the same string on the search page.

Each facet value is `(label, regex, cased)`, matching `tag_index.py`'s shape.
`cased` is True for acronyms and trade names, where a case-insensitive match
fires on ordinary words: `\\bTBP\\b` uncased matches nothing harmful, but `P507`
and `Y` most certainly do.

Two rules learned the hard way, both visible below:

* **Anchor short symbols.** Yttrium's symbol is `Y`, which appears in every
  chemical formula, axis label and variable name in the corpus. Element
  symbols are matched only in the oxidation-state and formula forms a paper
  actually writes -- `Y(III)`, `Y3+`, `Y2O3` -- never bare.
* **Match the class, not just the trade name.** `D2EHPA` and `HDEHP` are the
  same molecule under two names and must collapse to one label, or a reader
  filtering on one silently loses half the literature.
"""

from __future__ import annotations

# Element symbol -> name. Includes Sc and Y (rare earths by definition) and the
# Th/U pair, which is not a rare earth but travels with monazite and owns a
# chapter of the book.
ELEMENTS: list[tuple[str, str, int, int]] = [
    # (symbol, name, atomic number, group: 0 = LREE, 1 = HREE, 2 = adjacent)
    ("Sc", "scandium", 21, 2),
    ("Y", "yttrium", 39, 1),
    ("La", "lanthanum", 57, 0),
    ("Ce", "cerium", 58, 0),
    ("Pr", "praseodymium", 59, 0),
    ("Nd", "neodymium", 60, 0),
    ("Pm", "promethium", 61, 0),
    ("Sm", "samarium", 62, 0),
    ("Eu", "europium", 63, 1),
    ("Gd", "gadolinium", 64, 1),
    ("Tb", "terbium", 65, 1),
    ("Dy", "dysprosium", 66, 1),
    ("Ho", "holmium", 67, 1),
    ("Er", "erbium", 68, 1),
    ("Tm", "thulium", 69, 1),
    ("Yb", "ytterbium", 70, 1),
    ("Lu", "lutetium", 71, 1),
    ("Th", "thorium", 90, 2),
    ("U", "uranium", 92, 2),
]


def element_patterns(symbol: str, name: str) -> list[tuple[str, bool]]:
    """Regexes that mean "this paper is talking about this element".

    The bare symbol is deliberately absent. `U` is a variable, `Y` is an axis,
    `Er` is inside "Erbium" but also inside German, `Sc` is inside "Sci".
    Requiring a valence, a formula subscript or a hyphenated pair costs a few
    real mentions and removes a flood of false ones.
    """
    s = symbol
    return [
        (rf"\b{name}\b", False),
        (rf"(?<![A-Za-z]){s}\s*\(\s*(?:III|II|IV|3\+|0)\s*\)", True),   # Nd(III)
        (rf"(?<![A-Za-z]){s}\s*3\s*\+", True),                          # Nd3+
        (rf"(?<![A-Za-z]){s}2O3\b", True),                              # Nd2O3
        (rf"(?<![A-Za-z]){s}\d*(?:Cl|F|\(NO3\)|2\(SO4\)|\(OH\))", True),  # NdCl3
        (rf"(?<![A-Za-z]){s}/[A-Z][a-z]?(?![a-z])", True),              # Nd/Dy pair
        (rf"(?<![A-Za-z])[A-Z][a-z]?/{s}(?![a-z])", True),
    ]


# --- reagents -------------------------------------------------------------
# Label collapses synonyms: the trade name, the chemical name and the acronym
# a given journal happens to prefer all land on one chip.
EXTRACTANTS: list[tuple[str, str, bool]] = [
    ("D2EHPA", r"D2EHPA|HDEHP|DEHPA|di-?\(?2-ethylhexyl\)? *phosphoric", True),
    ("PC88A / P507", r"PC-?88A|\bP507\b|EHEHPA|HEH/EHP|2-ethylhexyl phosphonic", True),
    ("Cyanex 272", r"Cyanex[\s-]*272", True),
    ("Cyanex 301/302", r"Cyanex[\s-]*30[12]", True),
    ("Cyanex 923/925", r"Cyanex[\s-]*92[35]", True),
    ("TBP", r"\bTBP\b|tri-?butyl ?phosphate", True),
    ("TODGA", r"\bTODGA\b|tetraoctyl ?diglycolamide", True),
    ("diglycolamide", r"diglycolamides?|\bDGA\b", False),
    ("TOPO", r"\bTOPO\b|trioctylphosphine oxide", True),
    ("Aliquat 336", r"Aliquat[\s-]*336|methyltrioctylammonium", True),
    ("amine extractants", r"trioctylamine|\bTOA\b|Alamine[\s-]*336|primary amine N1923", True),
    ("versatic / naphthenic acid", r"versatic|naphthenic acid", False),
    ("aminopolycarboxylate", r"\bEDTA\b|\bDTPA\b|\bHEDTA\b|\bNTA\b|\bDCTA\b", True),
    ("carboxylic acid", r"\b(?:citric|oxalic|lactic|acetic|malonic) acid", False),
    ("crown ether", r"crown ethers?|\b18-crown-6\b|calix\[?\d*\]?arene|calixarene", False),
    ("ionic liquid", r"ionic liquids?|\b\[?C\d+mim\]?\b|imidazolium|phosphonium", False),
    ("deep eutectic solvent", r"deep eutectic solvents?|\bDESs?\b|choline chloride", True),
    ("hydroxamic acid", r"hydroxamic acid", False),
    ("phosphine oxide", r"phosphine oxides?|\bTRPO\b|\bCMPO\b", False),
]

TECHNIQUES: list[tuple[str, str, bool]] = [
    ("solvent extraction", r"solvent extraction|liquid[-–—]liquid extraction|\bSX\b", True),
    ("ion exchange", r"\bion[- ]exchange|cation resin|chelating resin", False),
    ("chromatography", r"chromatograph(?:y|ic)|\bHPLC\b|displacement chromatograph", False),
    ("precipitation", r"precipitation|oxalate precipit|double sulfate", False),
    ("selective crystallization", r"(?:selective|fractional|eutectic freeze) crystalli[sz]ation", False),
    ("membranes", r"\bmembranes?\b|supported liquid membrane|\bSLM\b|polymer inclusion|nanofiltration", True),
    ("adsorption / MOF", r"adsorption|adsorbents?|metal[-–]organic framework|\bMOFs?\b|ion[- ]imprinted", True),
    ("bioleaching / biosorption", r"bioleach|biosorption|biosorbent|microbial|\bfungal\b", False),
    ("biological / protein", r"lanmodulin|lanthanide[- ]binding tag|\bprotein\b|peptide|\bLanM\b", True),
    ("coacervate / ATPS", r"coacervat|aqueous biphasic|\bATPS\b", True),
    ("microfluidics", r"microfluidics?|\bdroplet\b|slug flow|numbering[- ]up", False),
    ("electrochemical", r"electrochemical|electrodeposition|electrowinning|molten[- ]salt electrolysis|electrolysis", False),
    ("electrophoresis", r"capillary electrophoresis|isotachophoresis|electromigration", False),
    ("roasting / halogenation", r"carbochlorination|chlorination|fluorination|roasting|\bcalcination\b", False),
    ("leaching", r"\bleach(?:ing|ed|ant)\b|lixiviant", False),
    ("flotation / beneficiation", r"\bflotation\b|beneficiation|gravity separation|magnetic separation", False),
    ("flash Joule heating", r"flash Joule heating|\bFJH\b", True),
    ("supercritical CO2", r"supercritical (?:CO2|carbon dioxide|fluid)", False),
    ("computational chemistry", r"\bDFT\b|density functional|molecular dynamics|\bMD simulation|ab initio|COSMO-RS", True),
    ("machine learning", r"machine learning|neural network|\bML model|deep learning|random forest|Gaussian process", False),
    ("process modeling", r"process simulation|flowsheet|Aspen|process model|optimi[sz]ation|mixer[- ]settler", False),
    ("high-throughput", r"high[- ]throughput|self[- ]driving lab|automated screening|robotic", False),
]

FEEDSTOCKS: list[tuple[str, str, bool]] = [
    ("bastnäsite", r"bastn[äa]e?site", False),
    ("monazite", r"monazite", False),
    ("xenotime", r"xenotime", False),
    ("ion-adsorption clay", r"ion[- ]adsorption (?:clays?|ores?|deposits?)|weathered crust|regolith", False),
    ("coal ash", r"coal (?:fly )?ash|fly ash|coal refuse|\bcoal\b", False),
    ("bauxite residue", r"red mud|bauxite residue", False),
    ("NdFeB magnet", r"NdFeB|Nd-?Fe-?B|permanent magnets?|magnet scrap", True),
    ("NiMH battery", r"NiMH|nickel[- ]metal hydride|battery scrap|spent batter", True),
    ("e-waste", r"e[- ]waste|WEEE|electronic waste|end[- ]of[- ]life", True),
    ("phosphogypsum", r"phosphogypsum|phosphoric acid|phosphate rock|apatite", False),
    ("produced water / brine", r"produced water|geothermal brine|\bbrines?\b|oilfield water|acid mine drainage", False),
    ("phosphors", r"phosphors?|fluorescent lamp|\bCRT\b", True),
    ("spent catalyst", r"spent catalyst|\bFCC catalyst", True),
    ("mine tailings", r"tailings|mine waste|slag\b", False),
    ("seawater", r"seawater|sea water|ocean", False),
]

# The facet groups, in the order the search page shows them. `element` and
# `topic` are filled by the tagging pass in `facet-tags.json`, not by regex --
# see build_facets.py for why.
GROUPS = [
    ("extractant", "Extractant / reagent", EXTRACTANTS),
    ("technique", "Technique", TECHNIQUES),
    ("feedstock", "Feedstock", FEEDSTOCKS),
]

# What a work is *for*. Assigned by the tagging pass, not by regex: the
# difference between a paper that measures a distribution ratio and one that
# designs a flowsheet around it is not a difference in vocabulary.
TOPICS = [
    ("fundamentals", "Fundamentals & mechanism"),
    ("process", "Process design & modeling"),
    ("recycling", "Recycling & urban mining"),
    ("primary", "Primary production & mining"),
    ("environment", "Environment, LCA & TEA"),
    ("supply", "Supply chain & policy"),
    ("characterization", "Characterization & analysis"),
    ("computational", "Computational & ML"),
    ("review", "Review article"),
]
