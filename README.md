# covid19fibrosis

## Overview 
The mathematical model describes the role of TGF-β in the progression of lung fibrosis in COVID19 patients.

## Mathematical modeling of progression of fibrosis with dysregulation of TGF-β in COVID19 patients

### Code Authors
Mohammad Aminul Islam and Ashlee N. Ford Versypt, 
Dept. of Chemical & Biological Engineering,
University at Buffalo, The State University of New York.

Corresponding author: A. N. Ford Versypt, ashleefv@buffalo.edu

### Scripts for model

* covid19fibrosis/COVID19-0.5.0-tissue_damage/config/PhysiCell_settings.xml
This file contains the model parameters. We changed the following parameters to perform case studies.
antiinflammatory_cytokine_secretion_rate_by_damagedSite, antiinflammatory_cytokine_secretion_rate_by_macrophage, and death_rate of residual (secreting agents).

* covid19fibrosis/COVID19-0.5.0-tissue_damage/custom_modules/epithelium_submodel.cpp This file contains the rule for epithelial cells. The death of an infected epithelial cell creates a secreting agent at the time and location of cell death.

* covid19fibrosis/COVID19-0.5.0-tissue_damage/custom_modules/immune_submodels.cpp This file contains the rules for macrophages, fibroblasts, and secreting agents.

* Other parts of the code are the same as the previous release: https://github.com/pc4covid19/pc4covid19/releases/tag/v5.0

### Set up of simulation environment, output, and analysis
* Install PhysiCell following the instruction at https://github.com/MathCancer/PhysiCell/blob/master/documentation/Quickstart.md 

* Go to COVID19-0.5.0-tissue_damage directory from terminal and type "make" to compile the code ".\COVID19" to start simulation

* Output files are saved in COVID19-0.5.0-tissue_damage/output/

* Data structure for output files is available at http://physicell.org/physicell-tools-python-loader/ 

* covid19fibrosis/Analysis/ folder contains files used to extract data and perform analysis

### Scripts for analysis
* create_replications.py This file runs replications of the model.

* Analysis.py This file plots the cells and substrate dynamics from replications.

* mean_response_of_replications.py This file contains the mean response of replications.

* Collagen_area_fraction.py This file plots the violin plot for the collagen area fraction.

* TGF_beta_fibroblast_collagen_fitting.py This file contains the fitting routine used for TGF-β dependent fibroblasts recruitment, and fibroblasts mediated collagen deposition.

* mean_response_comparison_between_cases.py This file compare mean response among different case studies.


### Plot Replication
The folder "Template of in silico experiments" contains template code for all the cases. First, create_replications.py file is used to generate 15 replications. Then Analysis.py file is run to extract the output data. After that, mean_response_of_replications.py file is used to plot mean responses from different cases.

### Figure 2
![Figure 2](/Figures/Fig2.png)
The template code (e.g., DM, D, and M for figure 2) and analysis files (create_replications.py, Analysis.py, mean_response_of_replications.py) are placed in the same folder. Sequential running of the analysis file will generate the outputs in folders plot, Collagen_contour, and Collagen_violin.

## Acknowledgements
Research reported in this publication was supported by the National Institute of General Medical Sciences of the National Institutes of Health under award number R35GM133763. The content is solely the responsibility of the authors and does not necessarily represent the offcial views of the National Institutes of Health.
