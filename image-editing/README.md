
### Procedure for running the code for round-trip image editing
1. Download the source code and then put it to a folder in the google drive. 
2. Upload and run BDIA_experiments.ipynb over google colab. (Note: one may need to change the work directory in BDIA_experiments.ipynb for proper running).  
   
Note: The parameter $\gamma$ in BDIA has a big impact on the resulting edited images. The recommanded range for $\gamma$ is [1.0, 0.92]. 

### Acknowledgement
The implementation for BDIA for the round-trip image editing depends heavly on the open-source of EDICT. The main python function for realizing BDIA-DDIM for round-trip image editing is $\textbf{BDIA}\_$$\textbf{stablediffusion}$ in bdia_edict_functions.py.   

