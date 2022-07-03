import keyGeneration,Confusion,Diffusion
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


img = plt.imread('sampleImage2.jpeg')

keyX,keyY = keyGeneration.generateKeys()

confusedImage = Confusion.getConfusedImage(img=img,key=keyX)

diffusedImage = Diffusion.getDiffusedImage(img=confusedImage,key=keyY)

figure, axis = plt.subplots(3, 2)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.626)
figure.suptitle('Encryption')
axis[0,0].imshow(img,cmap='gray')
axis[0,0].set_title('Original Image')
axis[0,1].hist(img.ravel(),256,[0,256])
axis[1,0].imshow(confusedImage,cmap='gray')
axis[1,0].set_title('Confused Image')
axis[1,1].hist(confusedImage.ravel(),256,[0,256])
axis[2,0].imshow(diffusedImage,cmap='gray')
axis[2,0].set_title('Diffused Image')
axis[2,1].hist(diffusedImage.ravel(),256,[0,256])
figure.savefig('encryptionPlots.png')
plt.show()

cv.imwrite('originalImage.jpg',img)
cv.imwrite('confusedImage.jpg',confusedImage)
cv.imwrite('encryptedImage.jpg',diffusedImage)