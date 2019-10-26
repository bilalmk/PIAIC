import os
import numpy as np
from PIL import Image as image
#import matplotlib.pylab as plt

rootDir="photos"
images = []

def resize_image():
    numArray = np.zeros([20,200,200,3])
    i = 0
    for _,_,fileList in os.walk(rootDir):
        for fname in fileList:
            ext = os.path.splitext(fname)[1]
            fileName = os.path.splitext(fname)[0]
            
            img1 = np.array(image.open(rootDir+"/"+fname).resize((200,200)))
            img1.save
            numArray[i] = img1
            i=i+1
    return numArray

def print_array(numArray):
    for i in range(len(numArray)):
        print(i)
        print(numArray[i])
        print("---------------------")

if __name__ == "__main__":
    numArray = resize_image()
    print_array(numArray)
else:
    print("error")