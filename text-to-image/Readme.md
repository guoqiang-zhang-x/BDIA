We implemented BDIA-DDIM over StableDiffusion V2.  In particular, we introduced an additional file "BDIAddim.py" in the folder of "stablediffusionV2/ldm/models/diffusion" for BDIA-DDIM. 

Steps to run the code: 
1. Download the pretrained model v2-1_512-ema-pruned.ckpt from the following link: https://huggingface.co/stabilityai/stable-diffusion-2-1-base/tree/main, and then put the model to the folder "checkpoints"
2. Run the python file "sample.py". The geneated images can be found in the "outputs" folder
