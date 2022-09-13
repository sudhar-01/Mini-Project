import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import Lorenz

def plotMap(x,y,z):
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(x, y, z, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Map")
    plt.show()

def takeMod256(x,y,z):
    x_256 = (x*pow(10,16))%256
    y_256 = (y*pow(10,16))%256
    z_256 = (z*pow(10,16))%256
    return x_256,y_256,z_256

def takeMod65536(x,y,z):
    x_65536 = (x*pow(10,16))%65536
    y_65536 = (y*pow(10,16))%65536
    z_65536 = (y*pow(10,16))%65536
    return x_65536,y_65536,z_65536

def saveInFile(x,y):
    np.savetxt('key_gen_X.csv', x, delimiter=",",fmt="%d")
    np.savetxt('key_gen_Y_256.csv', y, delimiter=",",fmt="%d")

def generateKeys():
    xs,ys,zs = Lorenz.lorenzOutput(num_steps=1100000,dt=0.01)
    #plotMap(xs,ys,zs)

    xs_256, ys_256, zs_256 = takeMod256(xs,ys,zs)
    xs_65536, ys_65536, zs_65536 = takeMod65536(xs,ys,zs)

    #removing elemnets greater than 65536
    xss = xs_65536[xs_65536<65536]
    yss = ys_65536[ys_65536<65536]
    xsss = xs_256[xs_256<256]

    #remove retundancy
    xss = pd.unique(xss)
    yss = pd.unique(yss)
    #xsss = pd.unique(xsss)
    
    #reducing the length of array to 65536
    xs = xss[0:65536]
    ys = yss[0:65536]
    
    x_256 = xsss[0:65536]
    x_2566 = np.empty((65536,1),dtype=int)
    for i in range(65536):
        x_2566[i] = int(x_256[i])

    xs_d = {}
    ys_d = {}
    x_256_d = {}

    xs_d_sorted = {}
    ys_d_sorted = {}
    x_256_d_sorted = {}

    # key = index
    # value = element value
    for i in range(65536):
        xs_d[i] = int(xss[i])
        ys_d[i] = int(yss[i])
        x_256_d[i] = int(xsss[i])

    #sorting the dictionary wrt values
    x = sorted(xs_d,key = xs_d.get)
    y = sorted(ys_d,key = ys_d.get)
    x256 = sorted(x_256_d,key=x_256_d.get)

    for w in x:
        xs_d_sorted[w] = xs_d[w]

    for w in y:
        ys_d_sorted[w] = ys_d[w]

    for w in x256:
        x_256_d_sorted[w] = x_256_d[w]

    #take only keys
    key_gen_x = list(xs_d_sorted.keys())
    key_gen_y = list(ys_d_sorted.keys())
#   key_gen_x256 = list(x_256_d_sorted.keys())

    key_gen_x = np.array(key_gen_x)
    key_gen_y = np.array(key_gen_y)
#  key_gen_x256 = np.array(key_gen_x256)
    saveInFile(key_gen_x,x_2566)
    
    return key_gen_x,x_2566




