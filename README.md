# covid19fibrosis

## Overview 
The mathematical model describes the role of TGF-β in the progression of lung fibrosis in COVID-19 patients.

## An agent-based modeling approach for lung fibrosis in response to COVID-19

### Code Authors
Mohammad Aminul Islam and Ashlee N. Ford Versypt, 
Dept. of Chemical & Biological Engineering,
University at Buffalo, The State University of New York.

Corresponding author: A. N. Ford Versypt, ashleefv@buffalo.edu

### Scripts for model
* covid19fibrosis/COVID19-0.5.0-tissue_damage/config/PhysiCell_settings.xml This file contains the model parameters. We changed the following parameters to perform case studies.
antiinflammatory_cytokine_secretion_rate_by_damagedSite, antiinflammatory_cytokine_secretion_rate_by_macrophage, and death_rate of residual (secreting agents). The corresponding highlighted c++ code block are available at [^1].

* covid19fibrosis/COVID19-0.5.0-tissue_damage/custom_modules/epithelium_submodel.cpp This file contains the rule for epithelial cells. The death of an infected epithelial cell creates a secreting agent at the time and location of cell death. The corresponding highlighted c++ code block are available at [^2].

* covid19fibrosis/COVID19-0.5.0-tissue_damage/custom_modules/immune_submodels.cpp This file contains the rules for macrophages, fibroblasts, and secreting agents. The corresponding highlighted c++ code block are available at [^3].

* Other parts of the code are the same as the previous release: https://github.com/pc4covid19/pc4covid19/releases/tag/v5.0

[^1]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/PhysiCell_settings.ipynb
[^2]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/epithelium_submodel.ipynb
[^3]: https://github.com/ashleefv/covid19fibrosis/blob/master/Highlighted%20c%2B%2B%20code%20block/immune_submodels.ipynb

### Setting up of simulation environment
* Install PhysiCell following the instruction at https://github.com/MathCancer/PhysiCell/blob/master/documentation/Quickstart.md. 

* The folder "Template of in silico experiments" [^4] contains template code for all the cases.

* All simulations are performed using PhysiCell version 1.7.2beta. 

* Data structure for output files is available at http://physicell.org/physicell-tools-python-loader/.

* Output files are saved in COVID19-0.5.0-tissue_damage/output/

[^4]: https://github.com/ashleefv/covid19fibrosis/tree/master/Template%20of%20in%20silico%20experiments

### Running simulation, output, and analysis

* Single_run.ipynb This file run, extract data, and plot for a single simulation [^5]. Alternatively, go to COVID19-0.5.0-tissue_damage directory from terminal and type "make" to compile the code ".\COVID19" to start simulation.

* create_replications.ipynb This file create and runs replications of the model [^6].

* Multi_run_analysis.ipynb This file extract data from multiple replications and plot mean responses [^7].

* Collagen_violin_plot.ipynb This file generate the violin plots to compare end point statistics for multiple cases [^8].

* TGF_beta_fibroblast_collagen_fitting.ipynb This file showed the fitting of TGF-β-dependent fibroblast recruitment [^9].

[^5]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Single_run.ipynb
[^6]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/create_replications.ipynb
[^7]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Multi_run_analysis.ipynb
[^8]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/Collagen_violin_plot.ipynb
[^9]: https://github.com/ashleefv/covid19fibrosis/blob/master/Analysis/TGF_beta_fibroblast_collagen_fitting.ipynb

## Acknowledgements
Research reported in this publication was supported by the National Institute of General Medical Sciences of the National Institutes of Health under award number R35GM133763. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.
