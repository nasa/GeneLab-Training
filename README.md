# GL4U RNAseq

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/nasa/GeneLab-Training/tree/GL4U_RNAseq_2024)  
*Click the button above to launch an interactive Gitpod workspace.*

<details id="understanding-gitpod-session-timeouts">
  <summary>⚠️ <strong>Important: Understand Gitpod Session Timeouts Before Launching Gitpod</strong></summary>

By default, Gitpod workspaces have an inactivity timeout of **30 minutes**. If there is no user input during this time, your workspace will stop. Additionally, if you close the Gitpod editor tab (but leave JupyterLab open), the timeout reduces to **5 minutes**. 

To avoid unexpected disconnections:

- **Keep both the Gitpod editor and JupyterLab tabs open while working.**

You can adjust your timeout settings (default: 30 minutes) in your [Gitpod User Preferences](https://gitpod.io/user/preferences).

</details>  

## Getting Started

> Note: Review the [section about Gitpod session timeouts](#understanding-gitpod-session-timeouts) and adjust your default timeout settings as needed.

To run these notebooks interactively, click the "Open in Gitpod" button above. This will launch a Gitpod workspace with JupyterLab and all necessary dependencies installed.

## Using Gitpod

When you open the project in Gitpod:

1. The environment will automatically be set up with all required tools, including Bioconductor packages.
2. JupyterLab will start automatically in the background.
3. A popup will open asking, "Do you want Gitpod Code to open the external website?" Close this tab.
4. Look for a message in the terminal that looks like this:
   ```
   [I 2024-09-24 23:11:05.891 ServerApp] http://username-repo-u5e17l5rwf3:8888/lab?token=ec15f9e7b1a7ce015f1be5567cdd74a74fc948a68759e17c
   [I 2024-09-24 23:11:05.891 ServerApp] http://127.0.0.1:8888/lab?token=ec15f9e7b1a7ce015f1be5567cdd74a74fc948a68759e17c
   ```
5. Control-click (or Command-click on Mac) on the URL starting with `http://127.0.0.1:8888/lab?token=...`. This will open JupyterLab in a new tab.
6. All notebooks and data files will be available in the JupyterLab interface.

## Contents

### GL4U RNAseq JNs
1. [RNAseq Data Processing](GL4U_RNAseq_JNs/01-RNAseq_processing.ipynb)
2. [RNAseq Data Analysis](GL4U_RNAseq_JNs/02-RNAseq_analysis.ipynb)

### OSD-104
* [OSD-104](OSD-104)
  - Directory holding the input files we will use in the GL4U RNAseq JNs to process RNAseq data from [OSD-104](https://osdr.nasa.gov/bio/repo/data/studies/OSD-104).