from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
def decodeDNA(s1):
    k = ''
    for i in s1:
        if i == 'A':
            k+='00'
        elif i == 'G':
            k+='01'
        elif i == 'C':
            k+='10'
        elif i == 'T':
            k+='11'
    return k

def encodeDNA(b):
    k = ""
    split_string = [b[i:i+2] for i in range(0, len(b), 2)]

    for p in split_string:
        if p == '00':
            k+='A'
        elif p == '01':
            k+='G'
        elif p == '10':
            k+='C'
        else:
            k+='T'
    return k

def getDNADiff(s1,s2):
    k = ''
    for i in range(4):
        if (s1[i] == 'A' and s2[i] == 'A') or (s1[i] == 'G' and s2[i] == 'G') or (s1[i] == 'C' and s2[i] == 'C') or (s1[i] == 'T' and s2[i] == 'T') :
            k+='A'
        elif (s1[i] == 'A' and s2[i] == 'C') or (s1[i] == 'C' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'A'):
            k+= 'C'
        elif (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'C' and s2[i] == 'T') or (s1[i] == 'G' and s2[i] == 'A') or (s1[i] == 'T' and s2[i] == 'C'):
            k+= 'G'
        elif (s1[i] == 'A' and s2[i] == 'T') or (s1[i] == 'C' and s2[i] == 'A') or (s1[i] == 'G' and s2[i] == 'C') or (s1[i] == 'T' and s2[i] == 'G'):
            k+= 'T'
    return k


def getDiffusedImage(img,key):

    img = np.reshape(img,(65536,1))
    binary_repr_v = np.vectorize(np.binary_repr)
    bin_arr = binary_repr_v(img, 8)

    key = np.reshape(key,(65536,1))
    binary_repr_v_k = np.vectorize(np.binary_repr)
    bin_arr_key = binary_repr_v_k(key, 8)
    bin_arr_sum= [None] * 65536 

    bin_arr = bin_arr.flatten()
    bin_arr_key = bin_arr_key.flatten()

    for c in range(65536):
        bin_arr[c] = encodeDNA(bin_arr[c])
        bin_arr_key[c] = encodeDNA(bin_arr_key[c])
        x = getDNADiff(str(bin_arr_key[c]),str(bin_arr[c]))
        x = decodeDNA(x)
        bin_arr_sum[c] = [int(x,2)] # binary to decimal

    bin_arr_sum = np.array(bin_arr_sum)
    diffusedImage = np.reshape(bin_arr_sum,(256,256))

    return diffusedImage

