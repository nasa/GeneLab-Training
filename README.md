# GL4U Intro 

The GL4U Intro Jupyter notebooks can be run either as a Docker container or directly in Gitpod. 

## Option 1: Using Docker

### Instructions

1. Pull the Docker image:
   ```
   docker pull quay.io/nasa_genelab/gl4u-intro-2024:1.0.0
   ```

2. Run the Docker container and expose port 8888:
   ```
   docker run -it -p 8888:8888 quay.io/nasa_genelab/gl4u-intro-2024:1.0.0
   ```

3. Once the container is running, Jupyter Lab will start automatically, you should see a URL with a token in your terminal. It should look something like this:
   ```
   [I 2024-10-23 02:16:43.487 ServerApp]     http://127.0.0.1:8888/lab?token=8ec2547a55dee7b19f27d5687a1d61847cb9b35713cb8f0b
   ```

6. Hold Ctrl (or Cmd on Mac) and click on the URL to open Jupyter Lab in your web browser.

## Option 2: Using Gitpod

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/nasa/GeneLab-Training/tree/GL4U_Intro_2024)  
*Click the button above to launch an interactive Gitpod workspace.*  

<details id="understanding-gitpod-session-timeouts">
  <summary>⚠️ <strong>Important: Understand Gitpod Session Timeouts Before Launching Gitpod</strong></summary>

By default, Gitpod workspaces have an inactivity timeout of **30 minutes**. If there is no user input during this time, your workspace will stop. Additionally, if you close the Gitpod editor tab (but leave JupyterLab open), the timeout reduces to **5 minutes**. 

To avoid unexpected disconnections:

- **Keep both the Gitpod editor and JupyterLab tabs open while working.**

You can adjust your timeout settings (default: 30 minutes) in your [Gitpod User Preferences](https://gitpod.io/user/preferences) as shown below:

<img src="images/gitpod-user-preferences.png" align="center" alt=""/>

</details>  

<br>

### Getting Started with Gitpod

> Note: Review the [section about Gitpod session timeouts](#understanding-gitpod-session-timeouts) and adjust your default timeout settings as needed.  

To run these notebooks interactively using Gitpod, click the "Open in Gitpod" button above. This will launch a Gitpod workspace with JupyterLab and all necessary dependencies installed.  

### Using Gitpod  

When you open the project in Gitpod:  

1. Wait for the environment to set up and JupyterLab to start in the background.
2. Look for a message in the terminal that contains the URL: http://127.0.0.1:8888/lab
   It will look similar to this:

   <img src="images/gitpod-jupyter-running.png" align="center" alt="Jupyter Server Running Message"/>

3. Click on this URL to open JupyterLab in a new tab.
4. All notebooks and data files will be available in the JupyterLab interface.

<br>

## Contents  

### GL4U Intro JNs  
1. [Introduction to Jupyter](GL4U_Intro_JNs/01-jupyter-intro.ipynb)
2. [Unix Introduction](GL4U_Intro_JNs/02-unix-intro.ipynb)
3. [R Introduction](GL4U_Intro_JNs/03-R-intro.ipynb)
4. [Sequencing Data Quality Control](GL4U_Intro_JNs/04-sequencing-data-QC.ipynb)

### intro  
* [intro](intro)
  - Directory holding the input files we will use in the GL4U Intro JNs

### GL4U Intro Lectures
1. [Introduction to NASA, Science Mission Directorate, Space Biology, Open Science Data Repository, and GeneLab](GL4U_Intro_Lectures/NASA_SB_OSDR_GL_Intro_2024_compressed.pdf)
2. [Introduction to the command line, Unix and R commands, and Jupyter](GL4U_Intro_Lectures/CL_R_Jupyter_Intro_2024.pdf)
3. [Overview of short read sequencing](GL4U_Intro_Lectures/Short_Read_Sequencing_Overview_2024_compressed.pdf)

<br>

## Troubleshooting Gitpod Time Out 

While completing the JNs in the Jupyter Lab environment, your GitPod session my timeout. If this happens, when you try to run a code cell in your JN you may get an error indicating that a folder or file is not found, as shown below:

![GitPot_TimeOut_JN_identified](https://github.com/user-attachments/assets/9a72cba3-64c6-4b54-bc9a-f9b5e635ecf7)

If this happens, look at the tab containing your GitPod terminal (the one that contained the link to the Jupyter Lab). You will likely see the "Timed Out" message shown below. You can re-start your session by click on the "Open Workspace" button as shown below:
> _Note: Once you restart your workspace, make sure you re-run all the code blocks to ensure all variables are re-set and output files are generated._

![GitPot_TimeOut_Terminal_identified](https://github.com/user-attachments/assets/91b2d26c-582c-415c-8e86-e52c2681f594)
