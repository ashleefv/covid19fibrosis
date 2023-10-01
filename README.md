# covid19fibrosis

## Overview 
The mathematical model describes the role of TGF-β in the progression of lung fibrosis in COVID-19 patients. The model is developed using PhysiCell - an open-source agent-based simulator to study tissue dynamics. PhysiCell is written in C++ and requires installation before running simulations (details in Section 1). Template codes, simulation procedure, and analysis codes are in Section 2. For a quick start, use Single_run.ipynb [^1]. Section 3 contains highlighted C++ code blocks and corresponding line numbers for modification of the model parameters and conditions.

[^1]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Single_run.ipynb
## An agent-based modeling approach for lung fibrosis in response to COVID-19

### Code Authors
Mohammad Aminul Islam and Ashlee N. Ford Versypt, 
Dept. of Chemical & Biological Engineering,
University at Buffalo, The State University of New York.

Corresponding author: A. N. Ford Versypt, ashleefv@buffalo.edu

### 1. Setting up of simulation environment
* Install PhysiCell following the instruction at https://github.com/MathCancer/PhysiCell/blob/master/documentation/Quickstart.md. 

* All simulations are performed using PhysiCell version 1.7.2beta. 


### 2. Running simulation, output, analysis, and validation

* The folder "Template of in silico experiments" [^2] contains template code for all the cases.

* Single_run.ipynb This file run, extract data, and plot for a single simulation [^1]. Alternatively, go to COVID19-0.5.0-tissue_damage directory from terminal and type "make" to compile the code ".\COVID19" to start simulation.

* create_replications.ipynb This file create and runs replications of the model [^3].

* Multi_run_analysis.ipynb This file extract data from multiple replications and plot mean responses [^4].

* Collagen_violin_plot.ipynb This file generate the violin plots to compare end point statistics for multiple cases [^5].

* TGF_beta_fibroblast_collagen_fitting.ipynb This file showed the fitting of TGF-β-dependent fibroblast recruitment [^6].

* Validation.ipynb This file show Model validation with experimental data of TGF-β, collagen, macrophages [^7].

[^2]: https://github.com/ashleefv/covid19fibrosis/tree/master/Template%20of%20in%20silico%20experiments
[^3]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/create_replications.ipynb
[^4]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Multi_run_analysis.ipynb
[^5]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Collagen_violin_plot.ipynb
[^6]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/TGF_beta_fibroblast_collagen_fitting.ipynb
[^7]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Validation/Validation.ipynb

### 3. Model scripts and code blocks to update parameters and rules
* config/PhysiCell_settings.xml This file contains the model parameters. The C++ code blocks and corresponding line numbers for the fibrosis model are available at [^8].

* custom_modules/epithelium_submodel.cpp This file contains the function and rules for epithelial cells. The C++ code blocks and corresponding line numbers are available at [^9].

* custom_modules/immune_submodels.cpp This file contains the rules for macrophages, fibroblasts, and activation of latent TGF-β from damaged sites. The C++ code blocks and corresponding line numbers are available at [^10].

* Other parts of the code are the same as the previous release: https://github.com/pc4covid19/pc4covid19/releases/tag/v5.0

[^8]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/PhysiCell_settings.ipynb
[^9]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/epithelium_submodel.ipynb
[^10]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/immune_submodels.ipynb



## Acknowledgements
Research reported in this publication was supported by the National Institute of General Medical Sciences of the National Institutes of Health under award number R35GM133763. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.
