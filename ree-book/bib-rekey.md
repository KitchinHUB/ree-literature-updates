# Bibliography re-key

Phase 1 assigned keys from the metadata as it stood before the DOI-recovery
and DOI-mismatch repairs. Entries whose `author` field was a `{Journal} Authors`
placeholder at that moment were keyed `anonYEARword`; the repairs later gave many
of them a real first author from CrossRef, leaving the key inconsistent with the
record it names. `tools/rekey_bib.py` recomputes those keys from the current
metadata using the project convention (`lastnameYEARword`) and re-sorts the file.

Entries still carrying no usable author keep their `anon` key: there the key is
an accurate statement of what is known about the record.

- Entries in `references.bib`: **422**
- Re-keyed: **171**
- Still `anon` (author missing or a placeholder): **21**
- Chapter files updated: **0** (no chapter cited an `anon` key directly;
  the source-document keys are resolved through `citation-key-map.json`)

## Renames

- `anon1973lanthanide` → `cockerill1973lanthanide`
- `anon1995supercritical` → `lin1995supercritical`
- `anon2002rapid` → `baker2002rapid`
- `anon2004convenient` → `izod2004convenient`
- `anon2004rare` → `meyer2004rare`
- `anon2011characterization` → `nguyen2011characterization`
- `anon2012thermodynamics` → `desbouis2012thermodynamics`
- `anon2014life` → `navarro2014life`
- `anon2015environmental` → `zaimes2015environmental`
- `anon2016neutron` → `stosch2016neutron`
- `anon2016numbering` → `kriel2016numbering`
- `anon2016raman` → `fieser2016raman`
- `anon2016rare` → `bonificio2016rare`
- `anon2016rarea` → `silachyov2016rare`
- `anon2016thermodynamics` → `ansari2016thermodynamics`
- `anon2016use` → `schramm2016use`
- `anon2017cracking` → `sadri2017cracking`
- `anon2017development` → `abbasi2017development`
- `anon2017electrochemical` → `abbasalizadeh2017electrochemical`
- `anon2017fast` → `chen2017fast`
- `anon2017life` → `browning2017life`
- `anon2017rationally` → `hatanaka2017rationally`
- `anon2017recovery` → `park2017recovery`
- `anon2017rhamnolipid` → `hogan2017rhamnolipid`
- `anon2017separation` → `yelkenci2017separation`
- `anon2018bioleaching` → `zhang2018bioleaching`
- `anon2018coordination` → `edington2018coordination`
- `anon2018leaching` → `zhou2018leaching`
- `anon2018micro` → `xu2018micro`
- `anon2018overview` → `chen2018overview`
- `anon2018recovering` → `ojima2018recovering`
- `anon2018supramolecular` → `li2018supramolecular`
- `anon2019characterization` → `chen2019characterization`
- `anon2019complexation` → `chen2019complexation`
- `anon2019droplet` → `stevenkurniawan2019droplet`
- `anon2019fluorination` → `pretorius2019fluorination`
- `anon2019mechanistic` → `zhang2019mechanistic`
- `anon2019oxidative` → `elizalde2019oxidative`
- `anon2019rare` → `khan2019rare`
- `anon2019selective` → `liu2019selective`
- `anon2019sustainable` → `prodius2019sustainable`
- `anon2019sustainablea` → `he2019sustainable`
- `anon2020biosorption` → `breuker2020biosorption`
- `anon2020biosorptiona` → `giese2020biosorption`
- `anon2020determination` → `cheng2020determination`
- `anon2020environmentally` → `arellanoruiz2020environmentally`
- `anon2020highly` → `depauw2020highly`
- `anon2020hydrometallurgical` → `zhang2020hydrometallurgical`
- `anon2020library` → `sharma2020library`
- `anon2020multivariate` → `teng2020multivariate`
- `anon2020progress` → `pak2020progress`
- `anon2020progressa` → `okamura2020progress`
- `anon2020rare` → `lukowiak2020rare`
- `anon2020rationally` → `boronski2020rationally`
- `anon2020removal` → `wang2020removal`
- `anon2020separation` → `ram2020separation`
- `anon2020separationa` → `dashti2020separation`
- `anon2020supercritical` → `zhang2020supercritical`
- `anon2021alkyl` → `szczesniak2021alkyl`
- `anon2021approaches` → `indelicato2021approaches`
- `anon2021critical` → `rasoulnia2021critical`
- `anon2021effect` → `hassas2021effect`
- `anon2021fundamental` → `larochelle2021fundamental`
- `anon2021method` → `jally2021method`
- `anon2021rare` → `heilmann2021rare`
- `anon2021separation` → `dybczynski2021separation`
- `anon2021theoretical` → `cheng2021theoretical`
- `anon2021theoreticala` → `liu2021theoretical`
- `anon2021thermodynamic` → `han2021thermodynamic`
- `anon2021versatile` → `pesavento2021versatile`
- `anon2022design` → `taylor2022design`
- `anon2022development` → `li2022development`
- `anon2022economic` → `uysal2022economic`
- `anon2022environmental` → `zapp2022environmental`
- `anon2022high` → `li2022high`
- `anon2022lca` → `wan2022lca`
- `anon2022molten` → `perezcardona2022molten`
- `anon2022phytomining` → `dinh2022phytomining`
- `anon2022pyrometallurgy` → `rafique2022pyrometallurgy`
- `anon2022rare` → `ortu2022rare`
- `anon2022rareb` → `bashiri2022rare`
- `anon2022recycling` → `fujita2022recycling`
- `anon2022selective` → `vazirihassas2022selective`
- `anon2022selectivea` → `zhao2022selective`
- `anon2022separation` → `li2022separation`
- `anon2022separationa` → `dewulf2022separation`
- `anon2023advances` → `doyo2023advances`
- `anon2023application` → `shakiba2023application`
- `anon2023biomining` → `vo2023biomining`
- `anon2023bioseparation` → `qian2023bioseparation`
- `anon2023cerium` → `moldoveanu2023cerium`
- `anon2023comparative` → `pathapati2023comparative`
- `anon2023deep` → `alizadeh2023deep`
- `anon2023extraction` → `li2023extraction`
- `anon2023gravity` → `sree2023gravity`
- `anon2023green` → `xu2023green`
- `anon2023ionic` → `binnemans2023ionic`
- `anon2023isothermal` → `bastos2023isothermal`
- `anon2023lanthanides` → `nikolova2023lanthanides`
- `anon2023latest` → `kaczorowska2023latest`
- `anon2023membrane` → `kujawa2023membrane`
- `anon2023mineral` → `ali2023mineral`
- `anon2023progress` → `elouardi2023progress`
- `anon2023rare` → `zheng2023rare`
- `anon2023recovery` → `zhang2023recovery`
- `anon2023recoverya` → `chung2023recovery`
- `anon2023simulation` → `turgeon2023simulation`
- `anon2023size` → `johnson2023size`
- `anon2023supercritical` → `zhu2023supercritical`
- `anon2023sustainable` → `elsayed2023sustainable`
- `anon2023work` → `alguacil2023work`
- `anon2024application` → `kore2024application`
- `anon2024chromatographic` → `belova2024chromatographic`
- `anon2024current` → `saravanan2024current`
- `anon2024eco` → `yu2024eco`
- `anon2024efficient` → `meng2024efficient`
- `anon2024enhanced` → `ortunomacias2024enhanced`
- `anon2024enhanceda` → `ge2024enhanced`
- `anon2024extraction` → `heo2024extraction`
- `anon2024extractiona` → `afonin2024extraction`
- `anon2024high` → `fernandezmaza2024high`
- `anon2024importance` → `summers2024importance`
- `anon2024industry` → `yang2024industry`
- `anon2024intensifying` → `he2024intensifying`
- `anon2024investigation` → `verma2024investigation`
- `anon2024investigationa` → `yang2024investigation`
- `anon2024investigationb` → `tolbert2024investigation`
- `anon2024mathematical` → `ding2024mathematical`
- `anon2024maximized` → `deng2024maximized`
- `anon2024mechanism` → `liu2024mechanism`
- `anon2024mechanisma` → `liu2024mechanisma`
- `anon2024methods` → `gkika2024methods`
- `anon2024microbial` → `vitova2024microbial`
- `anon2024modern` → `geue2024modern`
- `anon2024organic` → `wen2024organic`
- `anon2024overview` → `oztug2024overview`
- `anon2024polymer` → `croft2024polymer`
- `anon2024rare` → `ji2024rare`
- `anon2024rarea` → `bishop2024rare`
- `anon2024rationally` → `hu2024rationally`
- `anon2024research` → `liao2024research`
- `anon2024reshaping` → `chen2024reshaping`
- `anon2024scalable` → `good2024scalable`
- `anon2024separationa` → `li2024separation`
- `anon2024simple` → `oconnelldanes2024simple`
- `anon2024simplified` → `obrien2024simplified`
- `anon2024situ` → `lin2024situ`
- `anon2024spectroscopic` → `tse2024spectroscopic`
- `anon2024synergistic` → `zhang2024synergistic`
- `anon2025application` → `deng2025application`
- `anon2025clean` → `xue2025clean`
- `anon2025conversion` → `laskar2025conversion`
- `anon2025discovery` → `he2025discovery`
- `anon2025efficiently` → `he2025efficiently`
- `anon2025harnessing` → `bai2025harnessing`
- `anon2025high` → `schmitz2025high`
- `anon2025interactions` → `mcgaughey2025interactions`
- `anon2025iron` → `li2025iron`
- `anon2025metabolic` → `jiang2025metabolic`
- `anon2025microfluidic` → `feng2025microfluidic`
- `anon2025mine` → `song2025mine`
- `anon2025preparation` → `bulin2025preparation`
- `anon2025rare` → `hamzat2025rare`
- `anon2025rarea` → `karati2025rare`
- `anon2025reclaiming` → `nili2025reclaiming`
- `anon2025separation` → `lu2025separation`
- `anon2025sustainable` → `nadi2025sustainable`
- `anon2025sustainablea` → `agrawal2025sustainable`
- `anon2025systematic` → `mugion2025systematic`
- `anon2025tailored` → `salehi2025tailored`
- `anon2025technoeconomic` → `azimi2025technoeconomic`

## A later single rename (2026-09-06)

One further key was wrong for a different reason. `li2024lanthanide` came out of
the merge of `coacervate.bib` (`bibliography-audit.md:20` records it), and no
author of the paper is named Li: it is Ortuno Macias et al., *Lanthanide binding
peptide surfactants at air-aqueous interfaces*, PNAS 121(52) e2411763121. The
key was renamed to match the real first author, and the entry moved into
alphabetical order beside the group's 2025 foam-separation paper.

- `li2024lanthanide` → `ortunomacias2024lanthanide`

Four citation sites in `src/08-coacervates.md` and `src/11-biological-biomimetic.md`
were updated with it. `citation-key-map.json` and `citation-key-map.md` carry the
mapping so the converted org sources still resolve.
