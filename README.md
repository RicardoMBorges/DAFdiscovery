# DAFdiscovery
DAFdiscovery is meant to disseminate STOCSY calculation for NP scientists to enable data fusion and discovery of compounds of interest from correlation calculations.
The use of .csv files is meant to enable users to use their methods of choice for (MS and/or NMR) data processing. This method was developed from .csv derived from MNova and MZMine files.

Get Organized: Each project can be represented as its own directory inside the main directory of DAFdiscovery
* Download the main DAFdiscovery directory to a local of choice in your computer
* Each project should be organized as a new directory inside the main DAFdiscovery directory with all necessary inputs
* The STOCSY function is present at this main directory
* The .ipynb files (notebooks) are present in this main directory
	* users should copy and rename these .ipynb file (notebook) according to their projects 
	* users should delete unused options from each .ipynb file (notebook) according to their projects

Metadata (.csv) must include the following column headers

* Samples - sample codes

* MS_filename - MS filename as present at the MS derived .csv file if available
rows as the MS features 
columns as the samples
	
* NMR_filename - NMR filename as present at the NMR derived .csv file if available 
rows as the chemical shift (ppm) values
columns as the samples
	
* BioAct_filename - as reported for the BioActivity readout if available 

Important: The user is directed to different options according to the dataset available and made explicit in the Metadata. For instance, if the user has in the Metadata the columns Samples, MS_filename, and BioAct_filename, they will be pointed to option 4 (combining data from MS and Bioactivity).

Input files: .csv files were chosen as input because those are vendor-agnostic, easily handled by text editors, and we don't intent to re-create methods for peak processing for MS or NMR. Thus, users can process their data using their platform of choice (e.g.: MZmine for MS or MNova for NMR).

* Metadata.csv - presents a list of the filenames used for each dataset (MS, NMR, or BioActivity). Those filenames should be the same as exported from each specific processing platform (e.g.: MZmine for MS or MNova for NMR); they should list in ordem (according to the Samples column) all the headers from the other input .csv files

* MS.csv - the .csv file exported from the MS processing platform (e.g.: MZMine) where MS-features are listed as rows and samples as columns with filenames as headers for each column [tip: this can/should be the same \*quant.csv file used in FBMN from GNPS]

* NMR.csv - the .csv file exported from the NMR processing platform (e.g.: MNova) where chemical shifts are listed as rows and samples as columns with filenames as headers for each column

* BioActivity.csv - the .csv file produced from the Bioactivity readout where samples are listed headers for each column
	* a gradient of values (avoid binaries such as 'ative vs inactive' or '1 vs 0') for the Bioactivity data must be used since the potency of the activity will be a consequence of certain coumpound concentrations across samples


References:

https://pubmed.ncbi.nlm.nih.gov/15732908/

https://pubs.acs.org/doi/10.1021/ac051444m

https://pubmed.ncbi.nlm.nih.gov/35098600/

https://pubs.rsc.org/en/content/articlelanding/2019/fd/c8fd00227d
