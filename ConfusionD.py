import matplotlib.pyplot as plt
import numpy as np

def getOriginalImage(img,key):
    img_arr = np.reshape(img,(65536,1))
    k = np.array(img_arr[:,0],dtype=int)
    ori_image = np.zeros((65536,),dtype=int)
    for i in range(len(k)):
        ori_image[key[i]] = img_arr[i,0]
    ori_image = np.reshape(ori_image,(256,256))

    return ori_image
