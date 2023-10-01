# bash commands to download the data
#wget http://images.cocodataset.org/zips/val2014.zip
#wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip
#unzip annotations_trainval2014.zip -d coco/
#unzip val2014.zip -d coco/



import cv2
import os
import glob

def image_resize(path_source, path_des):

    if not os.path.exists(path_des):
        os.makedirs(path_des)

    fileList = glob.glob(os.path.join(path_source, "*.png"))

    for img_file in fileList:
        img = cv2.imread(img_file).astype(float)/255
        hei, width, _ = img.shape


        dim = min(hei, width)
        resized = cv2.resize(img, (int(width*256/dim),int(hei*256/dim)), interpolation = cv2.INTER_AREA)
        
        img_name = img_file.split('/')[-1].split('.')[0]
        cv2.imwrite(os.path.join(path_des,img_name+".jpg"),(resized*255).astype("uint8"))      
        
