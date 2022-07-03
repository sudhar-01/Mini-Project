import keyGeneration,ConfusionD,DiffusionD
import matplotlib.pyplot as plt
import numpy as np
encryptedImg = plt.imread('encryptedImage.jpg',0)

keyX = np.genfromtxt("key_gen_X.csv", delimiter=",",dtype=int)
keyY = np.genfromtxt("key_gen_Y_256.csv", delimiter=",",dtype=int)

diffusedImage = DiffusionD.getDiffusedImage(img=encryptedImg,key=keyY)

original = ConfusionD.getOriginalImage(img=diffusedImage,key=keyX)

figure, axis = plt.subplots(3, 2)
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.626)
figure.suptitle('Decryption')
axis[0,0].imshow(encryptedImg,cmap='gray')
axis[0,0].set_title('Encrypted Image')
axis[0,1].hist(encryptedImg.ravel(),256,[0,256])
axis[1,0].imshow(diffusedImage,cmap='gray')
axis[1,0].set_title('Diffused Image')
axis[1,1].hist(diffusedImage.ravel(),256,[0,256])
axis[2,0].imshow(original,cmap='gray')
axis[2,0].set_title('Original Image')
axis[2,1].hist(original.ravel(),256,[0,256])
figure.savefig('decryptionPlots.png')
plt.show()
