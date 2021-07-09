#DatasetSpilt.py
#Written by Olivia Yem, 13.6.2021
#A script to divide the cluster datasets into training, validation, and testing datasets.
#Will provide training, validation, and test folders, each with labels and images subfolders

import shutil
import glob
import numpy as np
from sklearn.model_selection import train_test_split

#create list of all images
folderPath = '/home/oliviayem/OctoberOnlyFruitletData/images'
imagePath = folderPath + '/*.jpg'
allFiles = np.array([]) #numpy array to hold all the files in the folder
for i in glob.glob(imagePath):
    #print(i)
    allFiles = np.append(allFiles,i)
print(len(allFiles))
#split images into training, validation and test sets
trainVal, test = train_test_split(allFiles, test_size=0.1, random_state=28)
training, validation = train_test_split(trainVal, test_size=0.11, random_state=28)
#copy images and labels into folders
for x in range(len(training)):
    originalImage = training[x]
    fileName = originalImage[len(folderPath)+1:-4]
    imageSavePath = '/home/oliviayem/DetectionDataset/training/images/'+fileName+'.jpg'
    shutil.copyfile(originalImage,imageSavePath)
    originalLabel = '/home/oliviayem/OctoberOnlyFruitletData/labels/'+fileName+'.xml'
    labelSavePath = '/home/oliviayem/DetectionDataset/training/labels/'+fileName+'.xml'
    shutil.copyfile(originalLabel,labelSavePath)
for y in range(len(validation)):
    originalImage = validation[y]
    fileName = originalImage[len(folderPath)+1:-4]
    imageSavePath = '/home/oliviayem/DetectionDataset/validation/images/'+fileName+'.jpg'
    shutil.copyfile(originalImage,imageSavePath)
    originalLabel = '/home/oliviayem/OctoberOnlyFruitletData/labels/'+fileName+'.xml'
    labelSavePath = '/home/oliviayem/DetectionDataset/validation/labels/'+fileName+'.xml'
    shutil.copyfile(originalLabel,labelSavePath)
for z in range(len(test)):
    originalImage = test[z]
    fileName = originalImage[len(folderPath)+1:-4]
    imageSavePath = '/home/oliviayem/DetectionDataset/test/images/'+fileName+'.jpg'
    shutil.copyfile(originalImage,imageSavePath)
    originalLabel = '/home/oliviayem/OctoberOnlyFruitletData/labels/'+fileName+'.xml'
    labelSavePath = '/home/oliviayem/DetectionDataset/test/labels/'+fileName+'.xml'
    shutil.copyfile(originalLabel,labelSavePath)