# Generate the Main Set of Processed RNAseq Data

During the bootcamp, participants will be processing [GLDS-104](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104/), RNAseq samples derived from the soleus (aka "anti-gravity") muscle of mice that were either flown in space aboard the International Space Station (ISS) (spaceflight, FLT) or kept in an environmental simulator on Earth to serve as ground controls (GC) during NASA's Rodent Research - 1 mission.

Prior to running the bootcamp, instructors must generate processed data for [GLDS-104](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104/) RNAseq FLT and GC samples using the [GeneLab RNAseq standard processing pipeline, revision A](https://github.com/nasa/GeneLab_Data_Processing/blob/master/RNAseq/Previous_GL-DPPD-7101_Revisions/GL-DPPD-7101-A.md). These data will be used as input when running the [RNAseq_fastq_to_counts_JN](../RNAseq_fastq_to_counts_JN) and [RNAseq_DGE_JN](../RNAseq_DGE_JN) Jupyter Notebooks to avoid having to wait for all participants' jobs to complete before moving to the next step in the pipeline. Using a set of pre-processed data will also help to minimize compute resource usage during the bootcamp by having each participant only process one sample from the dataset in real time. 

<br>

---

## RNAseq Tool Installation

Prior to running the [GLDS-104 processing scripts](GLDS-104_Processing_Scripts), all RNAseq data processing tools must be installed. Instructions for how to install these tools are located in the [RNAseq_Tool_Installation](RNAseq_Tool_Installation) subdirectory.

<br>

---

## GLDS-104 Processing Scripts

Exact processing scripts to generate the processed data for [GLDS-104](https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-104/) used in this bootcamp can be found in the [GLDS-104_Processing_Scripts](GLDS-104_Processing_Scripts) subdirectory. 
