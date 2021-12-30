import sys
sys.path.append('/home/nbuser/library/')
import pandas as pd
import copy
import math
from script import *
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
import numpy as np
from sklearn.cluster import KMeans
import os, shutil, glob, os.path
from PIL import Image as pil_image
from scipy.cluster.vq import vq
from scipy.spatial import distance


# La classe Vertex rappresenta i vertici di un grafo
class Preprocessing:
    def resize(self,setImages,h,w):
        dictImage={}
        for j in setImages.keys():
            listImage=[]
            for i in range(len(setImages[j])):
                res = cv2.resize(setImages[j][i], dsize=(h, w), interpolation=cv2.INTER_CUBIC)
                listImage.append(res)
            dictImage[j]=listImage
    
        return dictImage

    def intraclass_variance(self,dictImage):
        
        for j in dictImage.keys():
            mean1 = sum(dictImage[j])/len(dictImage[j])
            #after i calculate 
            variance = sum((dictImage[j] - mean1)**2)/(len(dictImage[j]) - 1);
            intraclassVar[sum(sum(variance))/(len(variance)**2)]=j
        return intraclassVar

    def cluster(self,dictImage,percent):
        dictCenter={}
        for j in dictImage.keys():
            listFlat=[]
            for i in range(len(dictImage[j])):
                result = dictImage[j][i].flatten()
                listFlat.append(result)
 
            kmeans = KMeans(n_clusters=(int(len(setImages[j])/percent)), random_state=0).fit(listFlat)
            dictCenter[j]=kmeans.cluster_centers_
            dictLabel[j]= kmeans.labels_
            dictFlat[j]=listFlat

        return (dictCenter, dictLabel, dictFlat)

    def ImageIndex(self,dictCenter,dictLabel,dictFlat):
        dictIndex={}
        for j in setImages.keys():
            listIndex=[]
            for i in range(len(dictCenter[j])):
                min=math.inf
                index=0
                for z in range(len(dictFlat[j])):
                    if(dictLabel[j][z]==i):
                        dst = distance.euclidean(dictCenter[j][i], dictFlat[j][z])
                        if(dst<min):
                            min=dst
                            index=z
                listIndex.append(index)
            dictIndex[j]=listIndex

        return dictIndex


    def spliTestTrain(self,dictImages,dictIndex):
        test = {}
        images = {}
        for j in dictImages.keys():
            listTest= [] 
            listTrain = []
            for i in range(len(dictImages[j])):
                if(i in dictIndex[j]):
                    listTest.append(dictImages[j][i])
                else:
                    listTrain.append(dictImages[j][i])
            test[j]=listTest
            images[j]=listTrain
        return (test,images)