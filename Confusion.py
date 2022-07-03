import matplotlib.pyplot as plt
import numpy as np

def getConfusedImage(img,key):
    img_arr = np.reshape(img,(65536,1))
    k = np.array(img_arr[:,0],dtype=int)
    confusedImg = np.zeros((65536,),dtype=int)

    for i in range(len(k)):
        confusedImg[i] = img_arr[key[i],0]

    confusedImg = np.reshape(confusedImg,(256,256))

    return confusedImg
