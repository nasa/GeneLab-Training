# GL4U RNAseq

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/nasa/GeneLab-Training/tree/GL4U_RNAseq_2024)  
*Click the button above to launch an interactive Gitpod workspace.*

<details id="understanding-gitpod-session-timeouts">
  <summary>⚠️ <strong>Important: Understand Gitpod Session Timeouts Before Launching Gitpod</strong></summary>

By default, Gitpod workspaces have an inactivity timeout of **30 minutes**. If there is no user input during this time, your workspace will stop. Additionally, if you close the Gitpod workspace tab, the timeout reduces to **5 minutes**.

If your workspace stops due to inactivity, you can restart it from your [Gitpod Workspaces](https://gitpod.io/workspaces) page. Look for your workspace in the list and click on its name to restart it.

For more details on workspace lifecycle and managing timeouts, see the [Gitpod Workspace Lifecycle Documentation](https://www.gitpod.io/docs/configure/workspaces/workspace-lifecycle).

</details>  

<br>

## Getting Started

To run these notebooks interactively, click the "Open in Gitpod" button above. This will launch a Gitpod workspace with VSCode, Jupyter, and all necessary dependencies installed. No additional setup is required.

<br>

## Using Gitpod

When you open the project in Gitpod:

1. **Wait for the environment to set up.** The VSCode editor will open within the Gitpod workspace.
2. **Navigate to the Notebooks:** In the VSCode interface, use the file explorer on the left to navigate to the Jupyter Notebooks (files ending with `.ipynb`).
3. **Open a Notebook:** Click on a notebook file to open it in the editor.
4. **Select the Appropriate Kernel:** Ensure that the correct kernel (Bash, Python, or R) is selected for each notebook. You can select the kernel by clicking on the kernel name at the top right corner of the notebook editor.
5. **Run Cells:** You can run the cells directly within VSCode by clicking on the Run button (▶️) to the left of the cell or pressing `Shift+Enter`.

> **Note:** Remember to save your work frequently. While Gitpod automatically saves changes, it's good practice to save to prevent data loss in case of a timeout.

<br>

## Contents

### GL4U RNAseq JNs
1. [RNAseq Data Processing](GL4U_RNAseq_JNs/01-RNAseq_processing.ipynb)
2. [RNAseq Data Analysis](GL4U_RNAseq_JNs/02-RNAseq_analysis.ipynb)

### OSD-104
* [OSD-104](OSD-104)
  - Directory holding the input files we will use in the GL4U RNAseq JNs to process RNAseq data from [OSD-104](https://osdr.nasa.gov/bio/repo/data/studies/OSD-104).

### GL4U RNAseq Lectures
1. [RNAseq Overview](GL4U_RNAseq_Lectures/RNAseq_Overview_2024_compressed.pdf) 

<br>

## Troubleshooting Gitpod Timeout 

Gitpod will time out after **30 minutes** of inactivity. When this happens, your workspace will stop, and a timeout message will be displayed.

![Gitpod Timeout Message](https://github.com/nasa/GeneLab-Training/blob/GL4U_Intro_2024/images/gitpod-timeout.png)

To restart your session:

1. **Go to your [Gitpod Workspaces](https://gitpod.io/workspaces) page.**
2. **Find your workspace in the list and click on its name to restart it.**
3. **Wait for the workspace to reload.**

> _Note: After restarting your workspace, make sure to re-run all code cells in your notebooks to reinitialize variables._

For more information on managing your workspaces, refer to the [Gitpod Workspace Lifecycle Documentation](https://www.gitpod.io/docs/configure/workspaces/workspace-lifecycle).
