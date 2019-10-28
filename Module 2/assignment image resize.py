import os
import numpy as np
from PIL import Image as image

rootDir="photos"
resizeFolderName = "resize"
images = []

def allowed_file(fileName):
    if fileName.endswith(".jpg") or fileName.endswith(".jpeg") or fileName.endswith(".png"):
        return True
    else:
        return False


def resize_image():
    arrayLength = len([name for name in os.listdir(rootDir) if name.endswith(".jpg") or name.endswith(".jpeg") or name.endswith(".png") ])
    numArray = np.zeros([arrayLength,200,200,3])
    i = 0

    for _,_,fileList in os.walk(rootDir):
        for fname in fileList:

            if(not os.path.exists(resizeFolderName)):
                os.makedirs(resizeFolderName)

            if(allowed_file(fname)):
                img = image.open(rootDir+"/"+fname)
                #width,height = img.size
                #if(width>=200 and height>=200):
                img = img.resize((200,200),image.ANTIALIAS)
                img.save(resizeFolderName+"/"+fname)
                numArray[i] = np.array(img)
                i=i+1
    return numArray

def print_array(numArray):
    for i in range(len(numArray)):
        print(i)
        print(numArray[i])
        print("---------------------")

if __name__ == "__main__":
    try:
        numArray = resize_image()
        print_array(numArray)
    except IOError:
        print("Can not resize image, file is not an image")
    except:
        print("Error occurred please try again")
else:
    print("error")