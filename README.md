# DAFdiscovery
DAFdiscovery is meant to disseminate STOCSY calculation for NP scientists to enable data fusion and discovery of compounds of interest from correlation calculations.
The use of .csv files is meant to enable users to use their methods of choice for (MS and/or NMR) data processing. This method was developed from .csv derived from MNova and MZMine files.

Input:
Metadata (.csv) must include the following column headers

Samples - sample codes

MS_filename - MS filename as present at the MS derived .csv file if available
rows as the MS features 
columns as the samples
	
NMR_filename - NMR filename as present at the NMR derived .csv file if available 
rows as the chemical shift (ppm) values
columns as the samples
	
BioAct_filename - as reported for the BioActivity readout if available 

References:
https://pubmed.ncbi.nlm.nih.gov/15732908/

https://pubs.acs.org/doi/10.1021/ac051444m

https://pubmed.ncbi.nlm.nih.gov/35098600/

https://pubs.rsc.org/en/content/articlelanding/2019/fd/c8fd00227d
