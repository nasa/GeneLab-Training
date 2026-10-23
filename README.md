# GL4U Capstone: RNA Sequence Data Analysis On Any OSD Dataset

During this hands-on activity, you will have the opportunity to analyze any RNA sequencing (RNAseq) dataset hosted on OSDR using a Jupyter Notebook (JN) within a Google Colab environment.  
> _Notes:_
> - _If you have not completed all activities from the [GL4U RNAseq Analysis JN](https://github.com/nasa/GeneLab-Training/blob/GL4U_RNAseq_2024_Colab/On-Demand/Access_Analysis_JN.md), please go back and complete those activities before this one._
> - _We'll be using Google Colab, so if you haven't done so already, follow [these instructions](https://github.com/nasa/GeneLab-Training/blob/GL4U_Intro_2024_Colab/On-Demand/Colab_Instructions.md) to set up your Google account and verify access to Google Colab._

<br>

## Files On This Branch

| File | Description |
|------|-------------|
| [`RNAseq_analysis_anyOSD_colab.ipynb`](RNAseq_analysis_anyOSD_colab.ipynb) | The Colab notebook used for this activity. It follows the differential gene expression (DGE) steps of the GeneLab RNAseq processing pipeline, [GL-DPPD-7101-G](https://github.com/nasa/GeneLab_Data_Processing/blob/master/RNAseq/Pipeline_GL-DPPD-7101_Versions/GL-DPPD-7101-G.md). |
| [`osdr_api_utils.py`](osdr_api_utils.py) | Python helper script used by the notebook to retrieve metadata and download data files from the [OSDR Biological Data API](https://visualization.osdr.nasa.gov/biodata/api/). **The notebook copies this file from this branch into your Google Drive automatically** (in the "Set up the notebook environment" section), so you do not need to download it yourself. |
| [`environment.yml`](environment.yml) | Conda environment for running the notebook locally (outside of Google Colab) with JupyterLab. Not needed for Google Colab. |
| [`README.md`](README.md) | These instructions. |

<br>

## Find An OSD Dataset To Analyze 

1. Before getting started, navigate to the [OSDR repository](https://osdr.nasa.gov/bio/repo/) and find a dataset you want to analyze.
   > _Note: If you are unfamiliar with the OSDR repository, review the [Access Data in the Open Science Data Repository](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/access_osdr_data.html) tutorial guide._

2. Click on the study link to navigate to the select OSD study page.
   > _Note: For study page assistance, review the [Navigate an OSDR Study Page](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/navigate_an_osdr_study_page.html) tutorial guide._

3. Once on the study page, make a note of the OSD identifier, as indicated in the screenshot below (you will need it for the hands-on activity; the matching GLDS identifier is retrieved automatically by the notebook). Also check the "Assay(s)" section of the study page to make sure that "RNA Sequencing (RNA-Seq)" is shown as one of the available Technologies for that dataset, as indicated below.
   > _Note: Some datasets contain more than one RNA Sequencing (RNA-Seq) assay (for example, [OSD-462](https://osdr.nasa.gov/bio/repo/data/studies/OSD-462) contains three, generated with different library preparation kits). The notebook will list the available RNAseq assays and let you choose which one to analyze._

<p align="center">
  <img src="https://raw.githubusercontent.com/nasa/GeneLab-Training/GL4U_RNAseq_2024_Colab/images/find_OSD_GLDS.png" width="800" height="800">
</p>

<br/>

4. The hands-on activity requires the `*genes.results` RSEM output files. Check to make sure your select dataset has these files available by looking in the Files section under the "GeneLab Processed RNA-Seq Files" -> "Raw Counts Data" folder, as shown in the screenshot below.
   > _Notes:_
   > - _If your select study does not have these files, go back to step 1 and search for a different dataset that does have the `*genes.results` RSEM output files available._
   > - _You do not need to download these files, you just need to make sure they exist for your select study. The notebook will download only the files of the samples you choose to analyze._

<p align="center">
  <img src="https://raw.githubusercontent.com/nasa/GeneLab-Training/GL4U_RNAseq_2024_Colab/images/check_for_rsem_files.png" width="800" height="800">
</p>

<br/>

<br>

## Access the RNAseq Analysis Of Any OSD Dataset Jupyter Notebook

1. If you are not already logged in to your Google account, go to [https://accounts.google.com/](https://accounts.google.com/) and log in.

2. Click on the "Open in Colab" icon below to open the notebook from this branch in Google Colab:
   > _Note: It is recommended to open the Colab notebook in a new tab so these instructions remain available._

   <a href="https://colab.research.google.com/github/nasa/GeneLab-Training/blob/GL4U_Capstone_DEV/RNAseq_analysis_anyOSD_colab.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

3. You should now see the RNAseq_analysis_anyOSD_colab.ipynb jupyter notebook (JN) opened in Google Colab.

4. Follow the instructions in the RNAseq_analysis_anyOSD_colab.ipynb JN to complete all activities. Read through the JN carefully so you do not miss any activities.
   > _Notes:_
   > - _When you run your first code cell in the Colab notebook, you may see the following pop-up. If you do, click "Run anyway" to continue, as shown below._
   > - _The first code cells mount your Google Drive (follow the pop-ups to allow access) and create the `NASA/GL4U/RNAseq` folder in "My Drive", where the `osdr_api_utils.py` helper script is copied from this branch and where all your output files will be stored._
   > - _Steps 0 and 1 of the JN use the **Python 3** runtime and Steps 2 through 6 use the **R** runtime. The JN tells you when to change the runtime type (**Runtime > Change runtime type**)._

<p align="center">
  <img src="https://raw.githubusercontent.com/nasa/GeneLab-Training/GL4U_RNAseq_2024_Colab/images/click_run_anyway_all-JNs.png" width="600" height="600">
</p>

<br/>

## Access Your Completed JN and Output Files

1. After you have completed all activities in the RNAseq_analysis_anyOSD_colab.ipynb JN and saved your completed JN to your Google Drive ("File" -> "Save a copy in Drive"), open [Google Drive](https://drive.google.com/drive/my-drive) in a new tab, and click "My Drive" in the left side panel, then double click on the "Colab Notebooks" folder as shown below.

<p align="center">
  <img src="https://raw.githubusercontent.com/nasa/GeneLab-Training/GL4U_RNAseq_2024_Colab/images/gd-open-colab-notebooks.png" width="800" height="800">
</p>

<br/>

2. You should see the "Copy of RNAseq_analysis_anyOSD_colab.ipynb" file in the "Colab Notebooks" folder.

   > _Note: Since this is not a required assignment in GL4U, you do not have to upload this JN to Canvas._

<br/>

3. To access the output files you generated for your select OSD/GLDS dataset, open [Google Drive](https://drive.google.com/drive/my-drive) in a new tab, and click on "My Drive" in the left side panel. Then double click on the "NASA" folder, then the "GL4U" folder, then the "RNAseq" folder, and finally the "OSD-###_GLDS-###" folder (note that the "###" should be the OSD and GLDS numbers of the dataset you processed), as shown below. Inside the "OSD-###_GLDS-###" folder, you will see all of the output folders that you created and the output files you generated for each respective step will be within that directory structure. 
 
<p align="center">
  <img src="https://raw.githubusercontent.com/nasa/GeneLab-Training/GL4U_RNAseq_2024_Colab/images/gd_OSD-GLDS_outputs_DGE.png" width="800" height="800">
</p>

<br/>

## Running the Notebook Outside of Google Colab (optional)

The notebook can also be run locally in JupyterLab. Create the conda environment from the `environment.yml` file on this branch, start JupyterLab, place `osdr_api_utils.py` next to the notebook (or let the notebook download it), then run the Python cells (Steps 0–1) with the Python 3 kernel and the R cells (Steps 2–6) with the R kernel. Outside of Colab, all files are stored in a `GL4U_RNAseq` folder inside the current working directory.

```bash
conda env create -f environment.yml
conda activate gl4u_rnaseq_2024
jupyter lab
```
