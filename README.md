# DAFdiscovery
DAFdiscovery is meant to disseminate STOCSY calculation for NP scientists to enable data fusion and discovery of compounds of interest from correlation calculations.
The use of .csv files is meant to enable users to use their methods of choice for (MS and/or NMR) data processing. This method was developed from .csv derived from MNova and MZMine files.

### Basics on Jupyter Notebook
* Jupyter Notebooks are completely free and users can download them on their own or as part of Anaconda (recommended) 
* Install Jupyter Notebooks through Anaconda at https://anaconda.org/
* Start Jupyter Notebooks from the Anaconda suite or using the 'Anaconda Prompt' (installed together with Anaconda)
	* we recommend adding the 'Anaconda prompt' to *favorites* (or Start in Windows) for easy access
	* from the 'Anaconda prompt', use jupyter notebook to start Jupyter Notebook
		* use jupyter notebook D: to start Jupyter Notebook at the driver D: (e.g. if Jupyter Notebook is in C: and data is in D:)
* Once Jyputer Notebook is opened, navigate to the directory where DAFdiscovery was saved to open the notebooks (.ipynb files)
* Dependencies required 
	* Open 'Anaconda Prompt' command line and install the packages:
		* NUMPY: type “pip install -U  numpy”
		* PANDAS: type “pip install -U  pandas”
		* IPYMPL: type “pip install -U  ipympl”
		* PLOTLY: type “pip install -U  plotly”
		* KALEIDO: type “pip install -U  kaleido”
		* MATPLOTLIC: type “pip install -U  matplotlib”
		* SKLEARN: type “pip install -U  scikit-learn”
		* SEABORN: type “pip install -U  seaborn”

* TIPS to know:
	* Jupyter is a web application used to create documents that integrate codes, information text, and results
		* each notebook document (.ipynb) is separated into cells that can be used for codes, texts, and others
		* Markdown: when a cell is set as Markdown, users can add text as a markup language to provide information for other users
		* Code: when a cell is set as Code, users can add code lines for programming
	* use %pwd to print the current directory
	* use %ls to show all files in the current directory
	* use %Who to list all variables
	* to run a cell with code lines, use "Ctrl + Enter" (or the button "Run")
	* Remember to always shutdown the kernel after using each notebook
		* Kernel --> Shutdown
* Have fun!

### Get Organized: Each project can be represented as its own directory inside the main directory of DAFdiscovery
* Download the main DAFdiscovery directory to a local of choice in your computer
* Each project should be organized as a new directory inside the main DAFdiscovery directory with all necessary inputs
* The STOCSY.py function is present at this main DAFdiscovery directory
* The .ipynb files (notebooks) should also be located in this main directory
	* users should copy and rename each .ipynb file (notebook) according to their projects 
	* users should delete unused options from each .ipynb file (notebook) according to their projects
![image](https://user-images.githubusercontent.com/15653685/175099663-78c0193d-9b96-4078-bffb-5138e5fc3cb7.png)

### Metadata (.csv) must include the following column headers

* Samples - sample codes

* MS_filename - MS filename as present at the MS derived .csv file if available
rows as the MS features 
columns as the samples
	
* NMR_filename - NMR filename as present at the NMR derived .csv file if available 
rows as the chemical shift (ppm) values
columns as the samples
	
* BioAct_filename - as reported for the BioActivity readout if available 

#### Important: Users are directed to different options according to the dataset available and made explicit in the Metadata. For instance, if the user has in the Metadata the columns Samples, MS_filename, and BioAct_filename, they will be pointed to option 4 (combining data from MS and Bioactivity).

### Input files: .csv files were chosen as input because those are vendor-agnostic, easily handled by text editors, and we don't intend to re-create methods for peak processing for MS or NMR. Thus, users can process their data using their platform of choice (e.g.: MZmine for MS or MNova for NMR).

* Metadata.csv - presents a list of the filenames used for each dataset (MS, NMR, or BioActivity). Those filenames should be the same as exported from each specific processing platform (e.g.: MZmine for MS or MNova for NMR); they should list in order (according to the Samples column) all the headers from the other input .csv files
![image](https://user-images.githubusercontent.com/15653685/175099437-b4a5a239-d044-4436-b3f7-92509ddd1354.png)

* MS.csv - the .csv file exported from the MS processing platform (e.g.: MZMine) where MS-features are listed as rows and samples as columns with filenames as headers for each column [tip: this can/should be the same \*quant.csv file used in FBMN from GNPS]
![image](https://user-images.githubusercontent.com/15653685/175099274-a4acdb5d-5dc2-4641-a975-12c35e4f76ed.png)

* NMR.csv - the .csv file exported from the NMR processing platform (e.g.: MNova) where chemical shifts are listed as rows and samples as columns with filenames as headers for each column
![image](https://user-images.githubusercontent.com/15653685/175099377-79b9e593-0342-4521-9f68-375aab28ac72.png)

* BioActivity.csv - the .csv file produced from the Bioactivity readout where samples are listed headers for each column
	* a gradient of values (avoid binaries such as 'active vs inactive' or '1 vs 0') for the Bioactivity data must be used since the potency of the activity will be a consequence of certain compound concentrations across samples

![image](https://user-images.githubusercontent.com/15653685/175099408-83a8b015-7418-4940-91f0-408dfb766321.png)

### References:

https://pubmed.ncbi.nlm.nih.gov/15732908/

https://pubs.acs.org/doi/10.1021/ac051444m

https://pubmed.ncbi.nlm.nih.gov/35098600/

https://pubs.rsc.org/en/content/articlelanding/2019/fd/c8fd00227d
