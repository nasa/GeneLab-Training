# Instructions for Setting Up the JupyterHub

The GL4U: June 2021 RNAseq Bootcamp was designed to run using a series of Jupyter Notebooks (JNs) that call tools for processing RNA sequence data using the [GeneLab RNA-seq consensus pipeline](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8044432/). To allow all bootcamp participants to run the JNs within the same environment, San Jose State University's (SJSU) system administrator, Steven Boring, set up a [JupyterHub](https://jupyter.org/hub) on the SJSU cluster, which runs the Red Hat Enterprise Linux (RHEL) CentOS operating system using the steps described within this directory.  

## Installing JupyterHub on a CentOS 7 HPC

The following instructions were modified from the [Install JupyterHub and JupyterLab from the ground up](https://github.com/jupyterhub/jupyterhub-the-hard-way/blob/HEAD/docs/installation-guide-hard.md) instructions, which provides a tutorial for installation of JupyterHub on an Ubuntu 18.04 system. The instructions below were modified to enable JupyterHub installation on the SJSU RHEL CentOS HPC.

> The SJSU HPC has the [Intel Distribution for Python](https://software.intel.com/content/www/us/en/develop/tools/oneapi/components/distribution-for-python.html#gs.8nrglu) installed, which is an [Anaconda](https://www.anaconda.com/) base Python distribution so conda commands can be used to create conda environments and install Python packages. On the SJSU HPC, the Intel Distribution for Python is installed in `/opt/intel/intelpython3/` so the environment created below will be saved in `/opt/intel/intelpython3/envs`. Be sure to change the paths in the instructions below to match your system environment.

<br>

## Part I: Create the JupyterHub environment, install, and configure JupyterHub

> Note: All the commands in this section are run as a superuser user like root. You can also precede each command with sudo if your account has sudo rights.

  **1. Create a conda environment named** `jupyterhub-env` **containing [JupyterHub](https://jupyter.org/hub), [JupyterLab](https://jupyter.org/), and [Jupyter Notebook](https://jupyter.org/) by running the following command:**

  ```
  conda create -n jupyterhub-env -c conda-forge jupyterhub jupyterlab notebook
  ```

  **2. Create the configuration file for JupyterHub by running the following commands:**

  > Note: This will create the default configuration file in `/opt/intel/intelpython3/envs/jupyterhub-env/etc/jupyterhub`. If this is different in your system, change the paths in the command below to match your system environment.

  ```
  mkdir -p /opt/intel/intelpython3/envs/jupyterhub-env/etc/jupyterhub/
  cd /opt/intel/intelpython3/envs/jupyterhub-env/etc/jupyterhub/
  /opt/intel/intelpython3/envs/jupyterhub-env/bin/jupyterhub --generate-config
  ```

  **3. Edit the configuration file to make the JupyterLab interface by default by setting the following configuration option in the** `jupyterhub_config.py` **file:**

  ```
  c.Spawner.default_url = '/lab'
  ```


  **4. Set up systemd**
  
  > To set up JupyterHub to run as a system service using systemd, which is responsible for managing all services that run at startup in Linux, create a service file in a suitable location in the `jupyterhub-env` environment folder then link it to the system services using the instructions below.


   a) Create the folder for the service file by running the following command:
  
   ```
   mkdir -p /opt/intel/intelpython3/envs/jupyterhub-env/etc/systemd
   ```
  
  
   b) Use a text editor to create the following text file:
    
   ```
   /opt/intel/intelpython3/envs/jupyterhub-env/etc/systemd/jupyterhub.service
   ```
    
    
   c) Paste the following service unit definition into the file you created in 4.b):
   
   > Note: This sets up the environment to use the virtual environment created, tells systemd how to start JupyterHub using the configuration file created in step 2, specifies that JupyterHub will be started as the root user (needed so that it can start Jupyter on behalf of other logged in users), and specifies that JupyterHub should start on boot after the network is enabled.
  
   ```
   [Unit]
   Description=JupyterHub
   After=syslog.target network.target
   
   [Service]
   User=root
   #Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/intel/intelpython3/envs/jupyterhub-env/bin:/opt/intel/intelpython3/bin"
   EnvironmentFile=/opt/intel/intelpython3/envs/jupyterhub-env/env-variables
   ExecStart=/opt/intel/intelpython3/envs/jupyterhub-env/bin/jupyterhub -f /opt/intel/intelpython3/envs/jupyterhub-env/etc/jupyterhub/jupyterhub_config.py
   
   [Install]
   WantedBy=multi-user.target
   ```


   d) Use a text editor to create the following file that will be read during the systemd start script to set up the environment variables used by JupyterHub:
    
   ```
   /opt/intel/intelpython3/envs/jupyterhub-env/env-variables
   ```
  
  
   e) Paste the following content into the file you created in 4.d):
    
   ```
   CONDA_DEFAULT_ENV=jupyterhub-env
   CONDA_EXE=/opt/intel/intelpython3/bin/conda
   CONDA_PREFIX_1=/opt/intel/intelpython3
   CONDA_PREFIX=/opt/intel/intelpython3/envs/jupyterhub-env
   CONDA_PROMPT_MODIFIER=(jupyterhub-env)
   CONDA_PYTHON_EXE=/opt/intel/intelpython3/bin/python
   _CONDA_PYTHON_SYSCONFIGDATA_NAME=_sysconfigdata_x86_64_conda_cos6_linux_gnu
   _CONDA_SET_PROJ_LIB=PROJ_LIB
   CONDA_SHLVL=2
   PATH=/opt/intel/intelpython3/envs/jupyterhub-env/bin/libfabric:/opt/intel/intelpython3/bin/libfabric:/opt/intel/intelpython3/envs/jupyterhub-env/bin:/opt/intel/intelpython3/condabin:/usr/local/sbin:/sbin:/bin:/usr/sbin:/usr/bin
   RSTUDIO_WHICH_R=/opt/intel/intelpython3/envs/jupyterhub-env/bin/R
   ```
 
 
   f) Make the systemd aware of the service file created in 4.b) by creating a symbolic link to the file in the systemd's directory by running the following command:
    
   ```
   ln -s /opt/intel/intelpython3/envs/jupyterhub-env/etc/systemd/jupyterhub.service /etc/systemd/system/jupyterhub.service
   ```
      
      
   g) Reload the systemd configuration files by running the following command:
    
   ```
   systemctl daemon-reload
   ```
    
    
   h) Enable the JupyterHub service by running the following command:
    
   ```
   systemctl enable jupyterhub.service
   ```
     
     
   i) The service will start on reboot, but it can be started without rebooting by running the following command:
    
   ```
   systemctl start jupyterhub.service
   ```
      
      
   j) Check that the JupyterHub service is running by executing the following command:
    
   ```
   systemctl status jupyterhub.service
   ```
      
<br>

## Part II: Configuring the reverse proxy

> Note: At this point the JupyterHub service will use `127.0.0.1:8000`. To make use of a cleaner url like `server_url/jupyter/`, set up a reverse proxy using the instrucitons below.

 **1. Configure JupyterHub to use the reverse proxy by modifying the** `jupyterhub_config.py` **file in** `/opt/intel/intelpython3/envs/jupyterhub-env/etc/jupyterhub` **as follows:**
 
   Change the `c.JupyterHub.bind_url` clause to `c.JupyterHub.bind_url = 'http://:8000/jupyter'`
 
 **2. Use a text editor to create a** `jupyterhub.conf` **file in the** `/etc/httpd/conf.d` **directory.**
 
 > Note: If httpd (apache) is not the web server used, create this file in the directory that corresponds to the web server used for your system. 
 
 **3. Add the following text to the** `jupyterhub.conf` **file created in step 2:**
 
  ```
  # SAMPLE CONFIG SNIPPETS FOR APACHE WEB SERVER
  #
  # This file contains examples of entries that need
  # to be incorporated into your Apache web server
  # configuration file.  Customize the paths, etc. as
  # needed to fit your system.
  
  <VirtualHost *:80>
      ProxyPreserveHost On
  
      RewriteEngine On
      RewriteCond %{HTTP:Connection} Upgrade [NC]
      RewriteCond %{HTTP:Upgrade} websocket [NC]
  
      RewriteRule /jupyter/(.*) ws://127.0.0.1:8000/jupyter/$1 [NE,P,L]
      RewriteRule /jupyter/(.*) http://127.0.0.1:8000/jupyter/$1 [NE,P,L]
  
      ProxyPass /jupyter/ http://127.0.0.1:8000/jupyter/
      ProxyPassReverse /jupyter/ http://127.0.0.1:8000/jupyter/
  </VirtualHost>
  ```
 
 **4. Restart the httpd service by running the following command:**
 
  ```
  systemctl restart httpd.service
  ```

**You should now be able to browse to the JupyterHub server via < http://server_url/jupyter/ > which should direct you to the JupyterHub login page. Once logged in, you will be taken to the JupyterLab interface.**

<br>

## Part III: Install RNAseq Tools and Kernels in JupyterHub

 **1. Add packages required to run the [RNAseq fastq to counts JN](../RNAseq_fastq_to_counts_JN) by executing the following command:**
 
  ```
  conda env update -n jupyterhub-env -f JupyterHub_fq_to_counts_tools.yml
  ```
 
 **2. Add packages required to run the [RNAseq DGE JN](../RNAseq_DGE_JN) by executing the following command:**
 
  ```
  conda env update -n jupyterhub-env -f JupyterHub_R_tools.yml
  ```
 
 **3. Make the `jupyterhub-env` conda environment visible to Jupyter by installing the Python kernel spec using either option a) or b) below:**
 
   a) Install the Python kernel spec into the JupyterHub virtual environment (`jupyterhub-env`) by running the following command:
   
   > Note: This ensures the spec overrides the default Python version and will only be visible to the JupyterHub installation created using the instructions detailed here. This is useful to avoid conda environments appearing where they are not expected.
  
   ```
   /opt/intel/intelpython3/envs/jupyterhub-env/bin/python -m ipykernel install --prefix=/opt/intel/intelpython3/envs/jupyterhub-env --name 'python-jupyterhub' --display-name "Python JupyterHub"
   ```

   b) Install the Python kernel spec system-wide by putting it into `/usr/local` by running the following command:
    
   > Note: This allows the spec to be visible to any parallel install of JupyterHub or JupyterLab and will persist even if you later delete or modify the JupyterHub installation. This is useful if the kernels might be used by other services, or if you want to modify the JupyterHub installation independently from the conda environments.
  
   ```
   /opt/conda/envs/python/bin/python -m ipykernel install --prefix /usr/local/ --name 'python' --display-name "Python (default)"
   ```

 **4. Install the R kernel spec via [CRAN](https://cran.r-project.org/) by running the following commands:**
 
   ```
   conda activate jupyterhub-env # activate the `jupyterhub-env` conda environemnt
   install.packages('IRkernel')
   IRkernel::installspec(user=false)  # to register the kernel in the current R installation
   ```
   
  > Note: By default `IRkernel::installspec()` will install a kernel with the name “ir” and a display name of “R” and will only install the kernel per-user. The `user=false` option will install the kernel system-wide.

