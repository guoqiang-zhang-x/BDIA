import os

#text_prompt = "a professional photograph of an astronaut riding a horse"
text_prompt = '"A man dressed for the snowy mountain looks at the camera"'

#ddim
folder_DDIM = "outputs/txt2img-samples_DDIM"
num_step  = 10
checkpoint = ".../v2-1_512-ema-pruned.ckpt"
cmd = 'python txt2img.py --ddim --prompt ' + text_prompt + ' --ckpt ' + checkpoint +' --config "configs/stable-diffusion/v2-inference.yaml" --steps ' +str(num_step)+  ' --n_iter 1 --outdir ' +folder_DDIM+  ' --device "cuda" --seed 1 --n_samples 3 --precision full'
os.system(cmd)


#BDIAddim
folder_BDIADDIM = "outputs/txt2img-samples_BDIADDIM"
num_step  = 10
gamma = 0.5 # the parameter gamma is within the range [0, 1]
checkpoint = ".../v2-1_512-ema-pruned.ckpt"
cmd = 'python txt2img.py --bdiaddim --gamma ' +str(gamma) + ' --prompt ' + text_prompt + ' --ckpt ' + checkpoint +' --config "configs/stable-diffusion/v2-inference.yaml" --steps ' +str(num_step)+  ' --n_iter 1 --outdir ' + folder_BDIADDIM +  ' --device "cuda" --seed 1 --n_samples 3 --precision full'
os.system(cmd)

