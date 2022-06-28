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
		* SCIKIT-LEARN: type “pip install -U  scikit-learn”
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
* Download the main DAFdiscovery directory to a local of choice on your computer
	* using the dropdown button "Code", click on Download ZIP to download the full contend
![image](https://user-images.githubusercontent.com/15653685/176012512-9bba2edd-0965-445c-acbb-1e51def8a917.png)

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




#### General input organization
![inputs-01-01](https://user-images.githubusercontent.com/15653685/175361394-2a0dc6c1-519d-40d9-a846-9688401fbac1.png)




### Running DAFdiscovery

* We recommend users to first open the notebook file "dafDiscovery_General.ipynb"

	* Notebooks will open as a new tab

* All notebooks are divided into cells and Code cells are the ones that should be used to run the codes

	* Markdown cells are used for information only and not to run codes

* To run a Code cell, users can use 'Ctrl + Enter' or the button "Run"

1. Dependencies to install

2. Import section

	2.a. Set the project to use

	2.b. Import the Metadata.csv file to establish filename order according to Sample IDs

		* this will define the option to be used regarding the available data. 

		* for e.g. if the user has 'MS_filename' and 'NMR_filename' only, this will direct the user to go for option 2 (work with MS and NMR data)

---
#### We recommend users delete other options and keep only the one that fits that project in use

##### Save the notebook file with another name (related to the project in use)
---

3. Data fusion

	3.a. in this cell, we will 

		* reorganize the filename order in each dataset according to the Sample IDs in the Metadata, 

		* merge the datasets accordingly

		* save the new merged dataset into a .csv file for the user to have it if necessary

4. STOCSY calculations

	4.a. in this cell, we will finally apply the STOCSY function to calculate the covariance and the correlation data from the selected driver peak

		* a driver peak must be selected/chosen by the user and it will reflect the user's interest in certain peak

		* a NMR peak can be used as driver if NMR data is available

		* a MS-feature can be used as driver if MS data is available

		* the bioactivity derived peak will be chosen when bioactivity data is available
			* this is because when we have bioactivity data, we want to look for (MS or NMR or both) peaks that are correlated to it
 
		* the resulted correlation values for each MS-feature (according to the selected driver) are saved as a .csv file names MSinfo_corr_*driver*.csv in the data directory created inside the Project directory in use

	4.b. to run the STOCSY calculation more than once, users can duplicate (Insert -> Insert Cell Below; or 'Esc + B') by copy and pasting the code into a new cell

		* the user will need to modify the driver again

	4.c. Plots

		* NMR STOCSY plots are so that the intensities correspond to the covariance values for each variable (according to the driver peak) and the colors correspond to the correlation values for each variable (according to the driver peak); the x-axis is kept as chemical shifts (ppm)

			* the color map refers to a variation between -1 to +1 where values close to 1 show strong correlations, but the signal shown negative or positive correlations

		* MS STOCSY plots are scatter-plots of Retention Time vs M/Z (this can be easily modified e.g. to Retention Time vs Row ID or scan ID)

		* MS-features are represented as circular marks with variable sizes and colors 

			* the sizes of the circular marks are related to the correlation values for each variable according to the driver

			* the color map refers to the same as mentioned before for the NMR STOCSY plot

	4.d. From DAFdiscovery to Cytoscape for Molecular Networks (FBMN-GNPS) when it is available 

		* the file MSinfo_corr_*driver*.csv produced after the application of the STOCSY function in a dataset that contains MS data can be imported as node attributes (in Cytoscape: File -> Import -> Table from File...)

		* this is possible because every correlation value is indexed to the 'row ID' which characterizes each deconvoluted MS-feature

		* this is why the user has an FBMN workflow and the required data available, for instance: the *_quant.csv file


### References:

https://pubmed.ncbi.nlm.nih.gov/15732908/

https://pubs.acs.org/doi/10.1021/ac051444m

https://pubmed.ncbi.nlm.nih.gov/35098600/

https://pubs.rsc.org/en/content/articlelanding/2019/fd/c8fd00227d

Video walk-through: https://youtu.be/_lQGzfK5V-k
