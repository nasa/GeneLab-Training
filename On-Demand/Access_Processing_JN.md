# RNA Sequence Data Processing 

During this hands-on activity, we will process an RNA sequencing (RNAseq) dataset hosted on OSDR using a Jupyter Notebook (JN) within a Jupyter Lab environment.  
> _Notes:_
> - _We'll be using GitPod, so if you haven't done so already, follow [these instructions](https://github.com/nasa/GeneLab-Training/blob/GL4U_Intro_2024/On-Demand/GitPod_Instructions.md) to get your GitPod account set up._
> - _This JN will be completed in two separate modules. If you are starting the hands-on activity in MODULE 3, you must re-run all steps completed in the hands-on activity in MODULE 2 before running the steps associated with MODULE 3._ 

<br>

## Access the RNAseq Processing Jupyter Notebook

1. **Open GitPod:** Click the button below to launch an interactive Gitpod workspace with JupyterLab and all necessary dependencies installed.
   
<div align="center">
    <a href="https://gitpod.io/#[https://github.com/nasa/Training/tree/GL4U_RNAseq_2024](https://github.com/nasa/GeneLab-Training/tree/GL4U_RNAseq_2024)">
        <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in Gitpod">
    </a>
</div>

<br>

2. When prompted, click "Continue" as shown below:  

![click_continue_rnaseq](https://github.com/user-attachments/assets/5ea43ee1-3c6d-4496-97d4-21136e144987)
  
3. You'll see the following icon indicating that the environment is setting up:  
   > _Note: It can take up to 10 minutes for the environment to set up._

![GitPod_setting-up](https://github.com/user-attachments/assets/cc107d6f-d07b-412e-aaf3-96933e63b797)

   
4. Once the environment finishes setting up, it will look as follows:
   > _Note: You can 'X' out of the pop-ups in the lower right corner._  

![Full_GitPod_rnaseq](https://github.com/user-attachments/assets/44a1825a-e297-4ca3-9f4b-68d66d2d1aaa)

<br>
   
5. Look for a message in the terminal that contains the URL: http://127.0.0.1:8888/lab
   It will look similar to this:  

![Jupyter_link_rnaseq](https://github.com/user-attachments/assets/203777cb-7825-4428-8499-e4ff41208001)

<br>

6. CMD+Click (Mac) or CTRL+Click (Windows) on that URL to open the Jupyter Lab environment in a new tab, which will look as follows:  
   > _Note: You can 'X' out of the pop-ups in the lower right corner._  

![Jupyter_Lab_rnaseq](https://github.com/user-attachments/assets/aceb17d4-7f58-4deb-8558-7a0ade2bfaae)

<br>

7. In the left side bar, double click on the "GL4U_RNAseq_JNs" folder as shown below:  

![GL4U_rnaseq_JNs_folder](https://github.com/user-attachments/assets/7b6fec78-80ab-445a-8740-0c2d4d653dab)


<br>

8. Then double click on the "01-RNAseq-processing.ipynb" file as shown below:  

![select_01-JN_rnaseq](https://github.com/user-attachments/assets/de403b0c-8790-4a86-9626-e5f85599ae81)

<br>

9. This will open the first of three Jupyter Notebooks (JNs), titled "RNAseq processing: fastq to counts":
   > _Note: The steps to be completed for MODULE 2 and MODULE 3 are indicated below._

![01-processing](https://github.com/user-attachments/assets/d3fa5516-7e34-4f48-8365-9fbd9d39e0fa)


<br>

10. Carefully read through the JN and complete all steps indicated for each MODULE and **be sure to save as you go by clicking CMD+S (Mac) or CTRL+S (Windows)**.
    - MODULE 2: Complete all activities in steps 0 - 2c of this JN.  
    - MODULE 3: Complete all activities in steps 3 - 8b of this JN.  
      > _Note: You must re-run steps 0 - 2c for the subsequent steps to run correctly._  

<br>

11. After you complete all steps assigned for your MODULE, download the JN to your computer by clicking "File" in the top left corner then "Download" as shown below:
    > _Note: Keep track of where on your computer you download your completed JN._  

![download](https://github.com/user-attachments/assets/0f73c1e1-3195-4365-ada9-b3a3b60b1bb5)

<br>

12. Next, export your completed JN as an HTML file by clicking "File" then "Save and Export Notebook As" then "HTML" as shown below:  
    > _Note: Keep track of where on your computer you download the HTML version of your completed JN._

![html](https://github.com/user-attachments/assets/f3a7a0ee-c4c7-45f4-a204-b23ca30553a7)

<br>

13. Shutdown your Jupyter Lab environment by clicking "File" then "Shut Down" and confirm your shutdown by clicking the "Shut Down" button in the pop-up window that appears as shown below:  

![shutdown_jupyter](https://github.com/user-attachments/assets/32cc3cb3-1af5-424e-9c13-2aab08bad6d3)

<br>

14. After Jupyter Lab shuts down, you will be returned to your GitPod environment. Once there, click on the three lines in the top left corner then click "Gitpod: Stop Workspace" as shown below.  

![stop_gitpod_workspace](https://github.com/user-attachments/assets/e855aaa0-b288-414b-b6b6-1e21c1ffa00a)

<br>

15. You will see your GitPod shutting down as indicated by the following icon:  

![stoping_gitpod](https://github.com/user-attachments/assets/b206ba30-32e3-4d20-bffd-dbcf5daa9cdf)


16. You are now ready to **return to Canvas and upload your completed JN and HTML files**, that you downloaded in steps 11 and 12 above, to show you successfully completed the steps of the JN assigned in this MODULE.

<br>

## Troubleshooting Gitpod Time Out 

While completing the JNs in the Jupyter Lab environment, your GitPod session my timeout. If this happens, when you try to run a code cell in your JN you may get an error indicating that a folder or file is not found, as shown below:

![GitPot_TimeOut_JN_identified](https://github.com/user-attachments/assets/9a72cba3-64c6-4b54-bc9a-f9b5e635ecf7)

If this happens, look at the tab containing your GitPod terminal (the one that contained the link to the Jupyter Lab). You will likely see the "Timed Out" message shown below. You can re-start your session by click on the "Open Workspace" button as shown below:
> _Note: Once you restart your workspace, make sure you re-run all the code blocks to ensure all variables are re-set and output files are generated._

![GitPot_TimeOut_Terminal_identified](https://github.com/user-attachments/assets/91b2d26c-582c-415c-8e86-e52c2681f594) 