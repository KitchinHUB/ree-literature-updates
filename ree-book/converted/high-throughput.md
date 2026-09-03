# Executive Summary

This literature review examines the state-of-the-art in high-throughput experimental methods for rare-earth element (REE) separations, with emphasis on:

- Automated liquid handling and robotic platforms
- Integration with analytical characterization (ICP-AES/ICP-MS)
- High-throughput synthesis and screening of extractants
- Machine learning integration for predictive modeling and optimization
- Active learning approaches for experimental design

Three key papers establish the foundation for automated REE separation research: cite:augustine2024advancing demonstrates machine learning-guided optimization using the LANL Super Separator for actinide separations; cite:an2024agile presents high-throughput synthesis and screening of diglycolamide extractants; and emerging work on machine learning prediction of distribution coefficients cite:liu2022advancing enables rational design of new extractants.

# 1. Automated High-Throughput Platforms for f-Element Separations
## 1.1 LANL Super Separator Platform
cite:augustine2024advancing developed a comprehensive automated platform that integrates robotic liquid handling with machine learning optimization for rare-earth (4f) and actinide (5f) separations.

### Platform Specifications

**Hardware Configuration:**

- Custom Big Kahuna automated instrument (Unchained Laboratories Inc.)
- Two robotic arms with automated liquid dispensing
  - Delivery accuracy: ±10 μL
  - Precision: ±5%
  - Maximum volume: 10 mL per dispense
- Six vortexers (2 temperature-controlled, 4 ambient)
- Integrated centrifugation for phase separation
- Radiologically compatible design for worker safety

**Throughput Capability:**

- Estimated ****200 measurements per day****
- Automated sample preparation, extraction, and characterization
- Rigorous control over experimental variables:
  - Analyte and extractant concentrations
  - pH and temperature
  - Contact times and mixing rates

### Machine Learning Integration: Bayesian Optimization

The platform employs Bayesian Optimization with Gaussian Process surrogate models to guide experimental design:

**Key Features:**

- Adaptive experimental design responding to real-time data
- Kriging Believer acquisition function for batch selection
- RBF and Matérn kernels for model flexibility
- Implementation in scikit-learn and scipy

**Performance Achievements:**

- Identified optimal conditions using only ****63% of experiments**** compared to full factorial screening
- ****74% reduction**** in experimental effort for four-dimensional optimization
- Convergence in 4 experimental cycles (339 total measurements vs. 1,296 for full screening)
- Optimal Th distribution ratio (D = 4.85 ± 0.8) achieved

### Case Study: Thorium Extraction Optimization

The platform was validated on Th⁴⁺ extraction using N,N-di-2-ethylhexylbutyramide (DEHBA) with TBP in n-dodecane.

**Optimized Conditions:**

- \[Th⁴⁺\]\_{feed} = 3.0 mM
- \[HNO₃\] = 4.0 M
- \[DEHBA\] = 40 mM
- Temperature = 25°C

**Human-in-the-Loop Safeguards:** The research team detected anomalous measurements (D = 6.58 ± 0.05) during cycle review that would have contaminated the Gaussian Process model. This demonstrates the value of expert oversight in automated optimization campaigns cite:augustine2024advancing.

## 1.2 Analytical Characterization Integration
### ICP-AES Protocol for Thorium Quantification

cite:augustine2024advancing implemented rigorous ICP-AES analysis:

**Instrumentation:** PerkinElmer Avio 500

**Critical Protocol Elements:**

- Seven-point calibration curve (0-10 ppm Th⁴⁺)
- Extended wash cycle: 50 seconds with 0.1 M HNO₃ + 0.01 w% HF
  - Prevents thorium adhesion to sample introduction hardware
  - Essential for accurate quantification
- Delay time: 65 seconds between samples
- Sample dilution: 10-1000× in 0.1 M HNO₃

### General ICP-MS/ICP-AES Automation

High-throughput elemental analysis requires seamless integration of liquid handlers with ICP instrumentation:

**FAST Automated Systems:**

- 2-5× faster than standard autosamplers
- Rapid vacuum sample loading with valve injection
- Optical sensors for automatic sample detection
- Analysis completed in \<3 minutes per sample for trace elements

**SimPrep Integration:**

- Automated sample dilution up to 1:2500
- Fully automated calibration standard preparation
- Compatible with ICP-OES and ICP-MS platforms

## 1.3 Data Management and Reproducibility
The LANL group deposited their complete dataset in the ****Separation Archive for f-elements (SAFE)**** at <https://safe.lanl.gov>, comprising 2,132 distribution ratios from literature involving 35 unique monoamide extractants and 11 actinide/lanthanide isotopes cite:augustine2024advancing.

# 2. High-Throughput Extractant Synthesis and Screening
## 2.1 Agile Diglycolamide Synthesis Platform
cite:an2024agile developed an integrated research, development, and deployment (RD&D) methodology combining facile ligand synthesis with rapid extraction evaluation.

### Green Chemistry Approach: Melt-Amidation

**Innovation:**

- Solvent-free melt-amidation coupling diglycolic acid with secondary amines
- No post-reaction workup or purification required
- Full conversion at 200°C

**Performance:**

- Scalable to ****200 grams****
- Yields: 85-96%
- Purities: 88-96%
- Substrate scope: 9 different DGA variants

**Environmental Impact:** Life cycle assessment revealed ****67% reduction in global warming potential**** compared to prior synthetic pathways cite:an2024agile.

**Advantages over Prior Art:**

- No pre-activation of diglycolic acid required
- Eliminates toxic organic solvents
- No toxic side-products or waste
- No tedious purification steps
- Reduced cost and process time
- Feasible industrial scale-up

### Automated Extraction Screening

**Throughput:** The automated workflow completed ****over 180 runs in 48 hours****, enabling rapid structure-activity relationship investigations of alkyl-substituted DGAs cite:an2024agile.

**Outcome:** The systematic ligand evaluation informed development of a promising flowsheet for separating light and heavy REEs.

## 2.2 Diglycolamide Extractant Advantages
Diglycolamide (DGA) extractants offer several advantages for REE separations:

- High extraction capacity
- Ease of synthesis (now enhanced by melt-amidation)
- Good thermal stability
- Good radiation stability
- Promising industrial applications

The work of cite:an2024agile demonstrates how integrating agile synthetic chemistry with automated screening accelerates discovery of sustainable extractants for critical materials.

# 3. Machine Learning for Distribution Coefficient Prediction
## 3.1 Deep Learning Approaches
cite:liu2022advancing developed deep neural networks (DNNs) trained on experimental data to predict distribution coefficients for lanthanide solvent extraction, enabling high-throughput virtual screening.

### Dataset and Model Performance

**Dataset:**

- 1,202 log D values collected from scientific literature
- Focused on single neutral ligands as extractants
- Covers lanthanide extraction across various conditions

**Model Architecture:**

- Combination of molecular physicochemical descriptors and atomic extended-connectivity fingerprints
- Deep neural network architecture

**Performance:**

- Best model: ****R² = 0.85****, ****RMSE = 0.53**** on validation set
- Successfully predicted D values for four novel ligand structures
- Experimental validation showed good agreement with predictions

### Practical Application

Distribution (D) values assess ligand performance:

- D \> 1: More than 50% of lanthanide extracted into organic solvent
- Enables rapid screening of ligand candidates without synthesis
- Accelerates rational design of selective extractants

## 3.2 Bayesian Optimization for Process Variables
Beyond ligand screening, cite:augustine2024advancing demonstrated that Bayesian Optimization with high-throughput robotics significantly accelerates optimization of extraction conditions (concentration, pH, temperature).

**Dataset Scope:**

- 2,132 distribution ratios from literature
- 35 unique monoamide extractants
- 11 different actinides and lanthanides

**Key Insight:** The combination of predictive modeling (for ligand selection) and adaptive experimentation (for process optimization) provides a complete workflow from molecular design to process conditions.

## 3.3 Explainable AI and Future Directions
Recent work (2025) developed explainable AI systems to predict REE leaching efficiency and provide real-time explanations of key extraction factors, trained on 572 experimental datasets.

This trend toward interpretable models will help identify underlying chemical principles governing selectivity and inform next-generation extractant design.

# 4. Integration of Computation and Experimentation
## 4.1 Computational Pre-Screening → Targeted Experiments
The emerging workflow combines:

1.  **Virtual screening** using ML models (cite:liu2022advancing)
    - Rapid prediction of log D for candidate ligands
    - Identification of promising structures
2.  **Automated synthesis** (cite:an2024agile)
    - Scalable, sustainable synthesis methods
    - High-throughput synthesis of top candidates
3.  **Automated extraction testing** (cite:augustine2024advancing)
    - Robotic platforms for systematic evaluation
    - ICP-AES/ICP-MS characterization
4.  **Process optimization** via Bayesian methods
    - Efficient exploration of multidimensional parameter space
    - Adaptive experimental design

## 4.2 Active Learning for Closed-Loop Discovery
While not yet extensively demonstrated in REE separations literature, active learning strategies show promise in related materials discovery applications:

- Polymer solar cells: ****75% reduction in discovery time**** through active learning
- Catalysts and batteries: Iterative experiment selection based on model uncertainty
- Potential application: Closed-loop systems combining ML prediction, robotic synthesis/testing, and adaptive sampling

****Gap Identified:**** Integration of active learning specifically for separations chemistry remains an emerging area with significant potential for future development.

# 5. Analytical Chemistry Considerations
## 5.1 Sample Throughput Requirements
For meaningful high-throughput separations research:

- Target: ****100-200+ measurements per day****
- Requires automation of sample preparation, extraction, and analysis
- ICP-AES/ICP-MS must integrate seamlessly with liquid handling

## 5.2 Critical Analytical Challenges
### For Actinides (Th, U, Pu):

- Surface adhesion to sample introduction systems
- Extended wash protocols required (cite:augustine2024advancing: 50 sec with HF)
- Radiological safety considerations
- Specialized facilities and protocols

### For Lanthanides:

- Spectral interferences in ICP-MS
- Matrix effects from high salt concentrations
- Need for appropriate sample dilution strategies
- Calibration across wide concentration ranges

## 5.3 Data Quality and Validation
High-throughput workflows require:

- Automated detection of outliers and anomalies
- Triplicate measurements for statistical confidence
- Human-in-the-loop review for quality assurance
- Standardized data formats and archiving (e.g., SAFE database)

# 6. Implications for Future REE Separation Platforms
## 6.1 Equipment Requirements for Bakery Square Lab
Based on the reviewed literature, a comprehensive REE separation platform would require:

### Core Robotic Capabilities:

- Automated liquid handler with multiple robotic arms
- Accurate dispensing (±10 μL or better)
- Temperature-controlled mixing/vortexing
- Automated centrifugation for phase separation
- High-throughput capability (100-200 samples/day)

### Analytical Characterization:

- ****ICP-AES or ICP-MS**** (critical gap if not currently available)
  - ICP-AES: Lower cost, suitable for major element quantification
  - ICP-MS: Higher sensitivity, better for trace analysis and isotopes
- Automated sample introduction system (e.g., FAST)
- Dilution/sample prep integration (e.g., SimPrep)

### Software Integration:

- Experiment design and workflow automation
- Real-time data acquisition from ICP
- Machine learning frameworks (Python/scikit-learn)
- Data management and archiving systems

## 6.2 Staffing Requirements
The reviewed literature suggests:

- ****Full-time postdoc or staff scientist**** with analytical chemistry expertise
  - Essential for ICP-AES/ICP-MS operation and method development
  - Quality control and data validation
  - Troubleshooting analytical issues (e.g., matrix effects, interferences)
- Computational support for ML integration
- Synthetic chemistry capability for extractant preparation

## 6.3 Research Program Scope
A high-throughput platform at Bakery Square could systematically explore:

### Extractant Screening:

- Commercial extractants: D2EHPA, PC88A, TBP, Cyanex series
- Novel extractant structures (DGAs, functionalized derivatives)
- Synergistic extractant mixtures

### Solvent Effects:

- Traditional: kerosene, dodecane
- Alternative diluents: alcohols, ketones, esters, ionic liquids
- Solvent mixtures and modifiers

### Process Variable Optimization:

- pH effects (particularly low pH, near 0)
- Temperature dependence
- Extractant and metal concentrations
- Contact time and mixing rates

### Comparative Studies:

- Selectivity across REE series (Y, La, Ce, Pr, Nd, Sm, Gd)
- Separation factors for critical pairs (e.g., Nd/Pr, Eu/Gd)
- Performance benchmarking

## 6.4 Integration with Computational Predictions
Following the workflow demonstrated by cite:augustine2024advancing and cite:liu2022advancing:

1.  Use ML models to predict log D for candidate extractants/conditions
2.  Prioritize experimental validation of top computational predictions
3.  Update models with new experimental data
4.  Iterate to refine predictions and explore chemical space efficiently

This hybrid computational-experimental approach could dramatically reduce the number of experiments required while maintaining comprehensive coverage of the design space.

# 7. Key Findings and Recommendations
## 7.1 State of the Art
### Demonstrated Capabilities:

- Automated platforms achieving ****200 measurements/day**** (cite:augustine2024advancing)
- ****74% reduction in experimental effort**** via Bayesian optimization
- High-throughput synthesis: ****180 runs in 48 hours**** (cite:an2024agile)
- ML prediction of log D: ****R² = 0.85**** (cite:liu2022advancing)
- ****67% reduction in environmental impact**** for sustainable synthesis

### Technology Readiness:

- Robotic liquid handling: Commercially available, proven for separations
- ICP-AES/ICP-MS automation: Established technology, requires method development
- Machine learning frameworks: Open-source tools (scikit-learn, scipy)
- Integration challenges: Require custom software and protocols

## 7.2 Critical Gaps Identified
1.  ****Active Learning for Separations:**** Limited literature on closed-loop active learning specifically for solvent extraction optimization

2.  ****Real-Time Analytics:**** Most platforms still require offline ICP analysis; online monitoring would further increase throughput

3.  ****Multi-Objective Optimization:**** Balancing selectivity, capacity, kinetics, and sustainability requires advanced optimization frameworks

4.  ****Standardized Data Formats:**** Beyond SAFE database, broader community standards would enable meta-analysis and transfer learning

## 7.3 Recommendations for CMU/METALLIC Collaboration
### Phase 1: Platform Assessment (3-6 months)

- Evaluate Bakery Square existing liquid handling capabilities
- Assess need for ICP-AES vs. ICP-MS
  - ICP-AES: Sufficient for log D measurements, lower cost
  - ICP-MS: Required for trace analysis, isotope studies
- Develop initial protocols for extraction workflows
- Hire analytical chemistry postdoc/staff

### Phase 2: Method Development (6-12 months)

- Validate platform with known REE/extractant systems (D2EHPA, PC88A)
- Benchmark against literature values (cite:liu2022advancing dataset)
- Optimize sample throughput and data quality
- Integrate ML prediction models

### Phase 3: Discovery Campaign (12-36 months)

- Systematic exploration of extractant/solvent space
- pH and temperature effects on selectivity
- Novel extractant screening (in collaboration with synthesis groups)
- Active learning implementation for adaptive experimentation

### Estimated Resource Requirements:

- **Personnel:** 1 FTE analytical chemist + computational support
- **Equipment:** ICP-AES (\~\$100-150K) or ICP-MS (\~\$200-400K) if not available
- **Consumables:** Extractants, solvents, standards, plasticware
- **Facilities:** Fume hoods, liquid handling robot (may be available at Bakery Square)

## 7.4 Synergy with Computational Modeling
The proposed computational work (ML-augmented prediction of extraction equilibria using DFT/UMA) would provide:

- Initial log D predictions to guide experimental priorities
- Understanding of structure-property relationships
- Hypothesis generation for novel extractant design

Experimental validation with a high-throughput platform would:

- Validate computational predictions
- Provide training data for model refinement
- Enable active learning loops
- Discover unanticipated chemical phenomena

This bidirectional coupling of computation and experimentation represents the frontier of accelerated materials discovery for critical element separations.

# References

bibliography:high-throughput-ree-refs.bib
