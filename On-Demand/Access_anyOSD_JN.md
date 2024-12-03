# RNA Sequence Data Analysis On Any OSD Dataset

During this (optional) hands-on activity, you will have the opportunity to analyze any RNA sequencing (RNAseq) dataset hosted on OSDR using a Jupyter Notebook (JN) within a Jupyter Lab environment.  
> _Notes:_
> - _If you have not completed all activities from the previous [RNAseq Analysis JN](Access_Analysis_JN.md), please go back and complete that activity before this one._
> - _We'll be using GitPod, so if you haven't done so already, follow [these instructions](https://github.com/nasa/GeneLab-Training/blob/GL4U_Intro_2024/On-Demand/GitPod_Instructions.md) to get your GitPod account set up._  

<br>

## Find An OSD Dataset To Analyze 

1. Before getting started, navigate to the [OSDR repository](https://osdr.nasa.gov/bio/repo/) and find a dataset you want to analyze.
   > _Note: If you are unfamiliar with the OSDR repository, review the [Access Data in the Open Science Data Repository](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/access_osdr_data.html) tutorial guide._

2. Click on the study link to navigate to the select OSD study page.
   > _Note: For study page assistance, review the [Navigate an OSDR Study Page](https://osdr-tutorials.readthedocs.io/en/latest/pages/guides/navigate_an_osdr_study_page.html) tutorial guide._

3. Once on the study page, make a note of the OSD identifier and the GLDS identifier, as indicated in the screenshot below (you will need these for the hands-on activity). Also check the "Assay(s)" section of the study page to make sure that "RNA Sequencing (RNA-Seq)" is shown as one of the available Technologies for that dataset, as indicated below.

![find_OSD_GLDS](https://github.com/user-attachments/assets/7580d897-5cda-4082-b215-e9ed73f0725e)

4. The hands-on activity requires the `*genes.results` RSEM output files. Check to make sure your select dataset has these files available by looking in the Files section under the "GeneLab Processed RNA-Seq Files" -> "Raw Counts Data" folder, as shown in the screenshot below.
   > _Notes:_
   > - _If your select study does not have these files, go back to step 1 and search for a different dataset that does have the `*genes.results` RSEM output files available._
   > - _You do not need to download these files, you just need to make sure they exist for your select study._

![check_for_rsem_files](https://github.com/user-attachments/assets/a63b5a68-538f-43ee-8c73-45f220500655)

<br>

## Access the RNAseq Analysis Of Any OSD/GLDS Dataset Jupyter Notebook

1. **Open GitPod:** Click the button below to launch an interactive Gitpod workspace with JupyterLab and all necessary dependencies installed.
   
<div align="center">
    <a href="https://gitpod.io/#https://github.com/nasa/GeneLab-Training/tree/GL4U_RNAseq_2024">
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

8. Then double click on the "03-RNAseq_analysis_anyOSD.ipynb" file as shown below:  

![select_03-JN_rnaseq](https://github.com/user-attachments/assets/e679a985-c580-4b16-9419-7577c8d38f96)

<br>

9. This will open the third of three Jupyter Notebooks (JNs), titled "RNAseq analysis of any OSD/GLDS dataset: DGE, annotations, and data visualization":

![03-anyGLDS](https://github.com/user-attachments/assets/fb42b4c3-96e8-4030-b7e7-3aa439c5172b)


<br>

10. Carefully read through the JN and complete all activities and **be sure to save as you go by clicking CMD+S (Mac) or CTRL+S (Windows)**. 

<br>

--- 

**Important notes and things to look out for while completing this JN:**

In step **0. Create Directory Structure for Processed Data**, make sure you change the OSD and GLDS identifiers to match the dataset you selected in the [Find An OSD Dataset To Analyze](#find-an-osd-dataset-to-analyze) above. 

![change_OSD_GLDS_bash](https://github.com/user-attachments/assets/9ff41a98-a109-4de1-aae5-0b134ebbdc4a)

<br>

Before you start step **2. Import and Format the Metadata and Data in R**, you must change your kernel from Bash to R by following the instructions below:

Click on the word "Bash" in the top right corner as shown below:

![change_kernel_1of3](https://github.com/user-attachments/assets/ccc9ad93-a47f-48ff-8bf4-9753f33916cb)

<br>

Open the drop-down menu and select "R" from the menu options as shown below:

![change_kernel_2of3](https://github.com/user-attachments/assets/41887922-04ee-4a38-97a0-21399abbba8d)

<br>

Once "R" is selected, click on the "Select" button as shown below. Then, check the top right corner of the JN to make sure you see that the R kernel is running as shown below:

![change_kernel_3of3](https://github.com/user-attachments/assets/4b73a785-d8ea-4a99-8e18-d92344219273)

<br>

In step **2b. Set up Directory Path Variables in R**, make sure you change the OSD and GLDS identifiers to match the dataset you selected in the [Find An OSD Dataset To Analyze](#find-an-osd-dataset-to-analyze) above. 

![change_OSD_GLDS_R](https://github.com/user-attachments/assets/25378a8e-3e1e-48bc-8d19-8fe2ad546e91)

<br>

--- 

<br>

11. Once complete, download the completed JN to your computer by clicking "File" in the top left corner then "Download" as shown below:
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


16. You are now ready to **return to Canvas and upload your completed JN and HTML files**, that you downloaded in steps 11 and 12 above, to show you successfully completed this hands-on activity.

<br>

## Troubleshooting Gitpod Time Out 

While completing the JNs in the Jupyter Lab environment, your GitPod session may timeout. If this happens, when you try to run a code cell in your JN you may get an error indicating that a folder or file is not found, as shown below:

![GitPot_TimeOut_JN_identified](https://github.com/user-attachments/assets/9a72cba3-64c6-4b54-bc9a-f9b5e635ecf7)

If this happens, look at the tab containing your GitPod terminal (the one that contained the link to the Jupyter Lab). You will likely see the "Timed Out" message shown below. You can re-start your session by clicking on the "Open Workspace" button as shown below:
> _Note: Once you restart your workspace, make sure you re-run all the code blocks to ensure all variables are re-set and output files are generated._

![GitPot_TimeOut_Terminal_identified](https://github.com/user-attachments/assets/91b2d26c-582c-415c-8e86-e52c2681f594) 
