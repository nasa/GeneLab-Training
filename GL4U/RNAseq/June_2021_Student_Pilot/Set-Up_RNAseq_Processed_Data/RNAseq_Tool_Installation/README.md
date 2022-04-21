# Instructions for installing tools required to process RNAseq data using the GeneLab pipeline

> **This directory holds yaml files and instructions for how to install two conda environments, [RNAseq_fq_to_counts_tools](RNAseq_fq_to_counts_tools.yml) and [RNAseq_R_tools](RNAseq_R_tools.yml), that contain all the software programs needed to generate the main set of [GLDS-104](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104/) processed RNAseq data used in this bootcamp. Additionally, instructions and scripts for creating the directory structure used in the [GLDS-104 processing scripts](../GLDS-104_Processing_Scripts) are provided.**  

---

### Install prerequisites

  * **Anaconda**  
    To install conda environments, you'll first have to install [Anaconda](https://www.anaconda.com/). Click [here](https://docs.anaconda.com/anaconda/install/) for installation instructions.

<br>

### Install the **RNAseq_fq_to_counts_tools** conda environment by running the following command:

  ```
  conda env create -f RNAseq_fq_to_counts_tools.yml
  ```

  Check proper installation by activating the RNAseq_fq_to_counts_tools conda environment with the following command:
  
  ```
  conda activate RNAseq_fq_to_counts_tools
  ``` 
  
  > Notes: 
  > - Depending on the configuration of the system used, the above command may not work, if that's the case try activating the conda environment with this command:
  > `source activate RNAseq_fq_to_counts_tools`
  > - This environment is activated when running scripts to generate the following main set of processed data:
  >   - [raw QC data](../GLDS-104_Processing_Scripts/00-RawData)
  >   - [trimmed and respective QC data](../GLDS-104_Processing_Scripts/01-TG_PreProc)
  >   - [alignment and respective QC data](../GLDS-104_Processing_Scripts/02-STAR_Alignment)
  >   - [count data](../GLDS-104_Processing_Scripts/03-RSEM_Counts)
  > - At least 45GB of RAM is required to run the tools in the RNAseq_fq_to_counts_tools conda environment.

<br>

### Install the **RNAseq_R_tools** conda environment by running the following command:

  ```
  conda env create -f RNAseq_R_tools.yml
  ```

  Check proper installation by activating the RNAseq_R_tools conda environment with the following command:
  
  ```
  conda activate RNAseq_R_tools
  ``` 
  > Notes: 
  > - Depending on the configuration of the system used, the above command may not work, if that's the case try activating the conda environment with this command:
  > `source activate RNAseq_R_tools`
  > - This environment is activated when running scripts to generate the following main set of processed data:
  >   - [DGE data](../GLDS-104_Processing_Scripts/04-05-DESeq2_NormCounts_DGE)
  > - The tools in the RNAseq_R_tools conda environment can be run on a standard laptop.

<br>

### Troubleshooting conda environment installation

  If you run into any issues while installing the RNAseq conda environments, update conda using the following command then try re-creating the RNAseq conda environments using the installation instructions above.
  ```
  conda update conda
  ```

<br>

### Create GLDS-104 RNAseq directory structure

  To generate the GLDS-104 RNAseq directory structure used to hold the main set of processed data called in the bootcamp training materials, follow the instructions below:
  1. Use the `cd` command to navigate to the location on your system where you want to create the GLDS-104 RNAseq directory structure.
     > Once there run the `pwd` command to show the path to this location, which will be needed to modify the [GLDS-104_Processing_Scripts](../GLDS-104_Processing_Scripts) as described in step 5ii.
  
  2. Download the [RNAseq_bc_June_2021_dir.sh](RNAseq_bc_June_2021_dir.sh) script into the location you navigated to in step 1 then run the command below to make the script executable:
     ```
     chmod u+x RNAseq_bc_June_2021_dir.sh
     ``` 
  
  3. Set up the directory structure by executing the [RNAseq_bc_June_2021_dir.sh](RNAseq_bc_June_2021_dir.sh) script using the following command:
     ```
     bash RNAseq_bc_June_2021_dir.sh
     ```  
  
  4. Navigate to the `/GLDS-104/Metadata` directory using the `cd` command as shown below and download the [GLDS-104_Group_Metadata.csv](GLDS-104_Group_Metadata.csv) and [organisms.csv](organisms.csv) files into that directory.
     ```
     cd GLDS-104/Metadata
     ``` 

5. Your directory structure should now be set up. To process GLDS-104 using the same scripts that were used to create the main set of processed data for this bootcamp, follow the steps below:  

   1. Download the scripts and associated input files found in [GLDS-104_Processing_Scripts](../GLDS-104_Processing_Scripts) into the respective subdirectories within the `GLDS-104/processing_scripts/` directory you made in step 3.   

   2. Use a text editor such as [nano](https://www.nano-editor.org/) to change the `/path/to` indicated in each of the processing scripts you downloaded in step 5i to match the path you navigated to in step 1.

      > **Notes:**
      > - The `/path/to` specified in the part of each script to activate the conda environment should be replaced with the path to where [anaconda3 was installed on your system](#install-prerequisites).
      > - If your system uses the [SLURM](https://slurm.schedmd.com/overview.html) job scheduler, you will also have to customize the #SBATCH options in each SLURM script to be consistent with your system's SLURM settings (consult your system administrator regarding the settings needed for your system).  
      > - If you are not using the slurm job scheduler, you will have to remove the #SBATCH options from each SLURM script and replace them with the equivalant options for the job scheduler your system uses.  
   
   3. Once you've downloaded the scripts and input data you need to start processing (step 5i) and have revised all of your processing scripts to indicate the correct paths and settings for your machine (step 5ii), you may use the `cd` command to navigate to the appropriare subdirectory within the `GLDS-104/processing_scripts` directory and begin executing the scripts as detailed in [GLDS-104_Processing_Scripts](../GLDS-104_Processing_Scripts).  
