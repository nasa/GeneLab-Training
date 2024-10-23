FROM jupyter/base-notebook

LABEL maintainer="alexis.torres@nasa.gov"
ENV TZ=America/Los_Angeles

USER root

# Install system utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    bsdmainutils && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Create workspace directory
RUN mkdir -p /workspace && chown jovyan:users /workspace

USER jovyan

# Clone the GL4U_Intro_2024 github branch
RUN git clone --single-branch --branch GL4U_Intro_2024 https://github.com/nasa/GeneLab-Training.git /workspace/GeneLab-Training

# Create conda environment from the cloned repository
RUN mamba env create -f /workspace/GeneLab-Training/environment.yml && \
    mamba clean -a -y

# Activate the conda environment and enable Jupyter extensions
RUN /bin/bash -c "source activate GL4U_Intro_JNs_2024 && \
    jupyter contrib nbextension install --user && \
    jupyter nbextensions_configurator enable --user"

# Set the working directory
WORKDIR /workspace/GeneLab-Training

# ENTRYPOINT set to conda environment
ENTRYPOINT ["/bin/bash", "-c", "source activate GL4U_Intro_JNs_2024 && exec \"$@\"", "--"]

# Run Jupyter Lab on initialization
CMD ["jupyter", "lab"]