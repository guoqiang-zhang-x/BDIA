# @title main(cleaned)

#from edict_functions import *

import edict_functions


import os
path = "img_edit_catgrass"
# Check whether the specified path exists or not
if not os.path.exists(path):
   os.makedirs(path)

# from jax._src.tree_util import tree_unflatten

PROMPT_EXTRA = ", hyper realistic, minutely detailed"

#EXPERIMENT = "dog1"
#EXPERIMENT = "dog2"
#EXPERIMENT = "dog3"
#EXPERIMENT = "dog4"
#EXPERIMENT = "dog5"
#EXPERIMENT = "dog7"
#EXPERIMENT = "dog8"
#EXPERIMENT = 'woman'
#EXPERIMENT = 'city_charlotte'
#EXPERIMENT = 'man'
#EXPERIMENT = 'plane'
#EXPERIMENT = 'cow'
#EXPERIMENT = 'car'
#EXPERIMENT = 'landscape'
#EXPERIMENT = 'cat'
EXPERIMENT = "dodiff"
#EXPERIMENT = "imagenetlake"
#EXPERIMENT = "catgrass"




if EXPERIMENT == "catgrass":
  #imgpath = 'experiment_images/highway-2498003_1280.jpg'
  imgpath = 'experiment_images/catgrass_original.png'
  base_prompt = 'a cat'
  prompt_list = [
                 ("lion",    "a lion in tall grass"),   # (filewrd, prompt)
                ]

if EXPERIMENT == "imagenetlake":
  #imgpath = 'experiment_images/highway-2498003_1280.jpg'
  imgpath = 'experiment_images/imagenet_lake.jpg'
  base_prompt = 'a lake'
  prompt_list = [#("bird",    "a bird above a lake"),   # (fileword, prompt)
                 ("ship",    "a ship in a lake"),   # (fileword, prompt)
                 ("castle", "A castle overlooking a lake"),
                 ("car", "A car stuck in a lake"),
                 ("fountain", "A fountain in a lake"),
                 ("helicopter", "a helicopter above a lake"),
                 #("elephant",    "a elephant on a lake"),   # (fileword, prompt)
                 #("rainy",   "a rainy city"),
                 #("UFO",    "a UFO above a lake"),   # (fileword, prompt)                
                 #("spiderman",    "Spiderman flying above a lake"),   # (fileword, prompt)                
                 #("batman",    "Batman flying above a lake"),   # (fileword, prompt)                
                 #("airship", "a airship above a lake"),
                 #("flood",   "a city after a flood"),
                 #("airplane", "an airplane flying above a city"),
                 #("moon", "a city with moon in the sky"),
                 #("helicopter", "a helicopter above a lake"),
                 #("eagle", "an eagle flying above a lake"),
                 #("castle", "a castle near a lake"),
                 #("house", "a house near a lake"),
                 #("future", "a futuristic modern city"), 
                ]

if EXPERIMENT == "landscape":
  #imgpath = 'experiment_images/highway-2498003_1280.jpg'
  imgpath = 'experiment_images/truebsee-5337646_1280.jpg'
  base_prompt = 'a lake'
  prompt_list = [#("bird",    "a bird above a lake"),   # (fileword, prompt)
                 ("ship",    "a ship in a lake"),   # (fileword, prompt)
                 #("elephant",    "a elephant on a lake"),   # (fileword, prompt)
                 #("rainy",   "a rainy city"),
                 #("UFO",    "a UFO above a lake"),   # (fileword, prompt)                
                 #("spiderman",    "Spiderman flying above a lake"),   # (fileword, prompt)                
                 #("batman",    "Batman flying above a lake"),   # (fileword, prompt)                
                 ("castle", "A castle overlooking a lake"),
                 ("car", "A car stuck in a lake"),
                 ("fountain", "A fountain in a lake"),
                 #("airship", "a airship above a lake"),
                 #("flood",   "a city after a flood"),
                 #("airplane", "an airplane flying above a city"),
                 #("moon", "a city with moon in the sky"),
                 ("helicopter", "a helicopter above a lake"),
                 #("eagle", "an eagle flying above a lake"),
                 #("castle", "a castle near a lake"),
                 #("house", "a house near a lake"),
                 #("future", "a futuristic modern city"), 
                ]

if EXPERIMENT == "city_charlotte":
  imgpath = 'experiment_images/charlotte-2069642_1280.jpg'
  base_prompt = 'a city'
  prompt_list = [("ufo",    "a UFO flying above a city"),   # (fileword, prompt)
                 #("rainy",   "a rainy city"),
                #("flood",   "a city after a flood"),
                 #("airplane", "an airplane flying above a city"),
                 #("moon", "a city with moon in the sky"),
                 ("helicopter", "a helicopter flying above a city"),
                 ("future", "a futuristic modern city"), 
                ]

if EXPERIMENT == "dog_puppy":
  imgpath = 'experiment_images/puppy-5124947_1280.jpg'
  base_prompt = 'a dog'
  prompt_list = [#("orange",    "an orange"),   # (fileword, prompt)
                  ("sand",    "a dog sits on sand"), 
                ]

if EXPERIMENT == "lake":
  imgpath = 'experiment_images/dolomites-2580866_1280.jpg'
  base_prompt = 'a lake'
  prompt_list = [#("orange",    "an orange"),   # (fileword, prompt)
                  ("bird",    "a bird above a lake"), 
                ]

if EXPERIMENT == "apple":
  imgpath = 'experiment_images/apple-256263_1280.jpg'
  base_prompt = 'an apple'
  prompt_list = [#("orange",    "an orange"),   # (fileword, prompt)
                  ("bird",    "a bird looking at an apple"), 
                ]


if EXPERIMENT == "dodiff":
  #imgpath = 'experiment_images/cat-551554_1280.jpg'
  #imgpath = 'experiment_images/imagenet_dog_2.jpg'
  #imgpath = 'experiment_images/imagenet_dog_6.jpg'
  #imgpath = 'experiment_images/dog-4253238_1280.jpg'
  #imgpath = 'experiment_images/wolf-8142720_1280.png'
  #imgpath = 'experiment_images/rabbit-2647220_1280.jpg'
  #imgpath = 'experiment_images/chicken-957795_1280.jpg'
  #imgpath = 'experiment_images/flower-50157_1280.jpg'
  #imgpath = 'experiment_images/animal-3414131_512.jpg'
  #imgpath = 'experiment_images/pixabay_boy.jpg'
  imgpath = 'experiment_images/man-67467_1280.jpg'
  


   
  base_prompt = 'a man'
  prompt_list = [#("blue_eye",    "a cat with blue eyes"),   # (fileword, prompt)
                #("green_eye",    "a cat with green eyes"),
                #("camera",    "a cat looking at the camera"),
                #("dog",    "a dog"),
                #("tiger", "a tiger"),
                #("monkey", "a monkey"),
                #("rabbit", "a rabbit"),
                #("monkey", "a monkey"),
                #("gorilla", "a gorilla"),
                #("rooster", "a rooster"),
                #("cat", "a cat"),
                #("chihuahua", "a chihuahua"),
                #("poodle",    "a poodle"),
                #("dalmatian",  "a dalmation"), 
                #("lion", "a lion"),
                #("donkey", "a donkey"),
                #("Leopard", "a Leopard"),
                #("sheep", "a sheep"),
                #("ferret", "a ferret"),
                #("flower", "a flower with red color"),   
                #("moon", "a dog on the moon"),  
                #("mask", "a boy wearing a mask"),
                ("manmask", "a man wearing a mask"),
                #("mustache", "a man with mustache"),
                ]

if EXPERIMENT == "cat":
  #imgpath = 'experiment_images/cat-551554_1280.jpg'
  imgpath = 'experiment_images/british-shorthair-6815375_1280.jpg'

  base_prompt = 'a cat'
  prompt_list = [#("blue_eye",    "a cat with blue eyes"),   # (fileword, prompt)
                #("green_eye",    "a cat with green eyes"),
                #("camera",    "a cat looking at the camera"),
                ("dog",    "a dog"),
                ("tiger", "a tiger"),
                ("rabbit", "a rabbit"),
                ("monkey", "a monkey"),
                ("gorilla", "a gorilla"),
                ("rooster", "a rooster"),  
                ]

if EXPERIMENT == "woman":
  imgpath = 'experiment_images/woman-657753_512.jpg'
  base_prompt = 'a photograph of a blonde woman' + PROMPT_EXTRA
  prompt_list = [("old",    "an old woman"),   # (fileword, prompt)
                 ("girl",  "a girl"),
                #("redhair",   "photograph of a woman with red hair" + PROMPT_EXTRA)
                 ("redhair",   "a woman with red hair")
                ]

if EXPERIMENT == "man":
  imgpath = 'experiment_images/pixabay_boy.jpg'
  #imgpath = 'experiment_images/beard-1845166_1280.jpg'
  #imgpath = 'experiment_images/man-3390927_1280.jpg'
  #imgpath = 'experiment_images/boy-1252771_1280.jpg'
  
  base_prompt = 'a boy' #+ PROMPT_EXTRA
  prompt_list = [#("old",    "an old man"),   # (fileword, prompt)
                 #("boy",  "a boy"),
                 ("blueeye",   "a boy with blue eyes"),
                 ("whitehair",   "a boy with white hair"),
                 #("black", "a boy with black hair"),
                ]

if EXPERIMENT == "car":
  #imgpath = 'experiment_images/pixabay_boy.jpg'
  #imgpath = 'experiment_images/mercedes-benz-1470136_1280.jpg'
  imgpath = 'experiment_images/maserati-gran-turismo-1649119_512.jpg'

  #base_prompt = 'a car' #+ PROMPT_EXTRA
  #prompt_list = [("tank",    "a military tank"),   # (fileword, prompt)
  #               #("boy",  "a boy"),
  #               # ("redhair",   "a man with red hair")
  #              ]
  base_prompt = "a sport car"
  prompt_list = [
                  ("submarine",    "a small futuristic submarine" ),
                 ("tank",      "an exotic futuristic military tank" ),
                 ("spaceship",    "a space fighter ship on the landing deck" ),
                ]

#if EXPERIMENT == "dog":
if "dog" in EXPERIMENT:
  if EXPERIMENT=="dog1":
    imgpath = 'experiment_images/imagenet_dog_1.jpg'
  elif EXPERIMENT=="dog2":
    imgpath = 'experiment_images/imagenet_dog_2.jpg' 
  elif EXPERIMENT=="dog3":
    imgpath = 'experiment_images/imagenet_dog_3.jpg'
  elif EXPERIMENT=="dog4":
    imgpath = 'experiment_images/imagenet_dog_4.jpg'     
  elif EXPERIMENT=="dog5":
    imgpath = 'experiment_images/imagenet_dog_5.jpg'
  elif EXPERIMENT=="dog6":
    imgpath = 'experiment_images/imagenet_dog_6.jpg'
  elif EXPERIMENT=="dog7":
    imgpath = 'experiment_images/imagenet_dog_7.jpg'
  elif EXPERIMENT=="dog8":
    imgpath = 'experiment_images/dog-5849152_1280.jpg'
    

  base_prompt = 'a dog'
  prompt_list = [("poodle",    "a poodle"),
                  ("dalmatian",  "a dalmation"),
                  #("G_R", "a Golden Retriever"),
                  ("chihuahua", "a chihuahua"), 
                  #("G_S", "a German Shepherd"),
                  #("husky", "a husky"),
                  #("moon",   "a black and whilte photo of a poodle dog on the moon" + PROMPT_EXTRA),
                ]


if EXPERIMENT == "monalisa":
  #imgpath = "images/monalisa_art-74050_512.png"
  imgpath = "experiment_images/art-74050_1280.jpg"
  
  base_prompt = "a woman"
  prompt_list = [
                 ("smile",    "a woman smiling" + PROMPT_EXTRA),
                 #("concert",    "a photo of a woman at a rock concert" + PROMPT_EXTRA),
                 # ("underwater",    "a photo portrait of a woman underwater with fish" + PROMPT_EXTRA),
                ]


if EXPERIMENT == "cow":
  #imgpath = "images/cow-2132526_512.png"
  imgpath = "experiment_images/cow-2132526_1280.jpg"
  
  #base_prompt = "a photograph of cow in a field"
  base_prompt = "a cow"
  
  prompt_list = [
                 #("black", "a black cow")
                 #("city",    "a cow in the city"),
                 ("horse",   "a horse"),              
                 #("city",    "a photograph of a cow in the city" + PROMPT_EXTRA),
                 #("desert",    "a cow in the desert"),
                ]

if EXPERIMENT == "plane":
  #imgpath = "images/plane-1506313_512.png"
  imgpath = "experiment_images/plane-1506313_1280.jpg"
  
  base_prompt = "a crashed plane"
  prompt_list = [("moon",    " a secret crashed spaceship on the moon"),
                 ("ufo",    "a crashed alien UFO wreckage" ),
                 ("desert",    "a crashed plane in the desert"),
                ]

im = edict_functions.load_im_into_format_from_path(imgpath)
im.save(f"{EXPERIMENT}_original.png","PNG")
gamma_list = [1.0, 0.96, 0.93] #[1.0, 0.98, 0.96, 0.93]
#mix_weight_list = [1.0, 0.98, 0.96, 0.93]
for gamma in gamma_list: 
#for mix_weight in mix_weight_list:
  for (i,e) in enumerate(prompt_list):
    edit_prompt = e[1]
    #print(edit_prompt)
    #outpath = f"BDIA_{EXPERIMENT}_{e[0]}.png"
    '''
    #EDICT performance
    outpath_EDICT = os.path.join(path,f"EDICT_{EXPERIMENT}_{e[0]}_scale_4_p_"+str(mix_weight)+".png")
    print(f"saving to {outpath_EDICT}")
    im_edit=edict_functions.EDICT_editing(imgpath, base_prompt, edit_prompt, mix_weight=mix_weight, guidance_scale=4, steps=50)
    im_edit[0].save(outpath_EDICT, "PNG")
    '''
    '''
    #BDIA performance
    outpath_BDIA = f"BDIA_{EXPERIMENT}_V3_{e[0]}_gamma_"+str(gamma)+".png"
    print(f"saving to {outpath_BDIA}")
    im_edit=edict_functions.BDIAV3_editing(imgpath, base_prompt, edit_prompt, gamma=gamma, steps=50)
    im_edit[0].save(outpath_BDIA, "PNG")
    '''
    '''
    #BDIA performance
    outpath_BDIA = f"BDIA_{EXPERIMENT}_V3_{e[0]}_gamma_"+str(gamma)+".png"
    print(f"saving to {outpath_BDIA}")
    im_edit=edict_functions.BDIAV3_editing(imgpath, base_prompt, edit_prompt, gamma=gamma, steps=50)
    im_edit[0].save(outpath_BDIA, "PNG")
    '''
    
    #BDIA performance
    outpath_BDIA = os.path.join(path, f"BDIA_{EXPERIMENT}_V5_{e[0]}_scale_4_gamma_"+str(gamma)+"_steps_40.png")
    print(f"saving to {outpath_BDIA}")
    im_edit=edict_functions.BDIAV5_editing(imgpath, base_prompt, edit_prompt, gamma=gamma, init_image_strength=0.8, guidance_scale=4, steps=50)
    im_edit[0].save(outpath_BDIA, "PNG")
    
    '''
    #BDIA performance
    outpath_CBDIA = os.path.join(path, f"CBDIA_{EXPERIMENT}_{e[0]}_scale_4_mix_weight_"+str(mix_weight)+".png")
    print(f"saving to {outpath_CBDIA}")
    im_edit=edict_functions.CBDIA_editing(imgpath, base_prompt, edit_prompt, mix_weight=mix_weight, init_image_strength=0.8, guidance_scale=4, steps=50)
    im_edit[0].save(outpath_CBDIA, "PNG")
    '''

    '''
    #BDIA performance with V7. V7 is equivalent is V5. The only diffence is that the code in V7 is much more simplified.     
    outpath_BDIA = os.path.join(path, f"BDIA_{EXPERIMENT}_V7_{e[0]}_gamma_"+str(gamma)+".png")
    print(f"saving to {outpath_BDIA}")
    im_edit=edict_functions.BDIAV7_editing(imgpath, base_prompt, edit_prompt, gamma=gamma, init_image_strength=0.8, guidance_scale=3, steps=50)
    im_edit[0].save(outpath_BDIA, "PNG")
    '''
    '''
    #BDIA performance with V8. test V8 to see if we can use a pair (y,z) 
    outpath_BDIA = os.path.join(path, f"BDIA_{EXPERIMENT}_V8_{e[0]}_gamma_"+str(gamma)+".png")
    print(f"saving to {outpath_BDIA}")
    im_edit=edict_functions.BDIAV8_editing(imgpath, base_prompt, edit_prompt, gamma=gamma, init_image_strength=0.8, guidance_scale=3, steps=50)
    im_edit[0].save(outpath_BDIA, "PNG")
    '''
    '''
    #DDIM performance
    outpath_DDIM = os.path.join(path,f"DDIM_{EXPERIMENT}_scale_4_{e[0]}.png")
    print(f"saving to {outpath_DDIM}")
    im_edit=edict_functions.EDICT_editing(imgpath, base_prompt, edit_prompt, guidance_scale=4, steps=50, run_baseline=True)
    im_edit[0].save(outpath_DDIM, "PNG")
    '''
  