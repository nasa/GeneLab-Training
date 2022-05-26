# GL4U: June 2022 RNAseq Educator Bootcamp - Pilot

This directory holds the bootcamp setup instructions and training materials used for the pilot GL4U: RNA sequencing (RNAseq) Educator Bootcamp, which was developed through a collaboration between [NASA GeneLab](https://genelab.nasa.gov/) and the [Jet Propulsion Laboratory (JPL) Planetary Protection Center of Excellence’s (PPCoE)](https://planetaryprotection.jpl.nasa.gov/) Virtual Opportunities for BIoinformatiCs RESearch (VOICES) program, and utilizes the [NASA Center for Climate Simulation, NCCS](https://www.nccs.nasa.gov/) [Science Managed Could Environment, SMCE](https://www.nccs.nasa.gov/systems/SMCE) system for compute resources. The pilot GL4U: RNAseq Educator Bootcamp contains materials similar to the [2021 GL4U: RNAseq Student Bootcamp](../June_2021_Student_Pilot), including introductory command line and space biology-specific lectures, hands-on instruction via Jupyter Notebooks (JNs) for running general Unix and R commands and for processing RNAseq data using [GeneLab's RNAseq standard processing pipeline, version D](https://github.com/nasa/GeneLab_Data_Processing/blob/master/RNAseq/Pipeline_GL-DPPD-7101_Versions/GL-DPPD-7101-D.md), but also contains instructions for educators to subsequently teach the bootcamp content at their home institution. These materials were organized into a week and a half long training program as detailed in the [schedule](Bootcamp_Schedule.md). The entire bootcamp will be recorded and the recordings will be uploaded [here](), broken up based on each day of instruction indicated in the [schedule](Bootcamp_Schedule.md).

---
## Bootcamp Setup Instructions
To run the GL4U: RNAseq Bootcamp at your home institution, instructors must request a time slot for resources on the NCCS SMCE system and accounts to be set up for all students who plan to participate. The instructions to request resources and accounts, as well as details about how to get started can be found in: 
- [NCCS_SMCE_Bootcamp_Setup](NCCS_SMCE_Bootcamp_Setup)

---
## Training Materials
Throughout the bootcamp, instruction transitions between lectures and hands-on training. In the links below, we provide 4 complete slide decks for each major topic covered, and those same slide decks split-up into sections based on when the material was taught during the week and a half long bootcamp. We also provide 4 JNs that contain the hands-on training corresponing to the lecture material, as well as completed versions of each JN. For information about when each section of the JNs were taught during the bootcamp see the [schedule](Bootcamp_Schedule.md). 

|Bootcamp [Lectures](Lectures)|Corresponding hands-on training via JNs|
|:---------------------------:|:-------------------------------------:|
|[Introduction to NASA, Space Biology, GeneLab, JPL PP VOICES, and the Command Line](Lectures/NASA_GL_CL_Intro)|[How to set up and run basic Unix and R commands on the command line and through the JN environment](Intro_JNs)|
|[RNAseq and Data Processing Overview](Lectures/RNAseq_Overview)|[Process raw RNAseq data from GLDS-104 to generate gene count data](RNAseq_fastq_to_counts_JN)|
|[Overview of the Statistics Used for RNAseq Data Analysis](Lectures/Statistics_Intro)|[Analyze RNAseq gene count data to generate differential gene expression data and corresponding visualizations](RNAseq_DGE_JN)|
|[Overview of Planetary Protection Metagenomics Projects](Lectures/PP_Metagenomics_Overview)|N/A|

---
### Content Contributors
The following people have developed the content and instructions for running this bootcamp:
- Amanda Saravia-Butler (GeneLab Data Processing)
- Lauren Sanders (GeneLab Data Processing)
- Philip Heller (San Jose State University, Assistant Professor)
- Alvin Smith (JPL PPCoE)
- Arman Seuylemezian (JPL PPCoE)
- Lisa Guan (JPL PPCoE)

---
### Compute Resources
- NASA NCCS SMCE Team (NASA Goddard Space Flight Center, Greenbelt, MD)
