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


# La classe di preprocessing è quella che permette di fare il preprocessing
# I dati sono arganizzati tramite dizionari, ogni dizionario ha come valore di 
# key-value ===>   'nome classe: lista di array nxn che rappresentano le immagini
# appartenenti a quella classe.


class Preprocessing:


    #Resize di tutte le immagini
    def resize(self,setImages,h,w):
        dictImage={}
        for j in setImages.keys():
            listImage=[]
            for i in range(len(setImages[j])):
                res = cv2.resize(setImages[j][i], dsize=(h, w), interpolation=cv2.INTER_CUBIC)
                listImage.append(res)
            dictImage[j]=listImage
    
        return dictImage
    #funzione che calcola la varianza intraclass
    def intraclass_variance(self,dictImages):
        
        intraclassVar={}
        for j in dictImages.keys():
            #For each class i calculate the Variance
            mean1 = sum(dictImages[j])/len(dictImages[j])
            variance = sum((dictImages[j] - mean1)**2)/(len(dictImages[j]) - 1);
            intraclassVar[sum(sum(variance))/(len(variance)**2)]=j
        return intraclassVar



    #cluster che trova i centroidi da usare come train
    #Prende in input la percentuale di trai i test che vogliamo avere
    #Restituisce come output 3 dizionari:
    # +++ dictCenter['nome_classe']= centroidi trovati per quella classe
    # +++ dictLabel['nome_classe']= label associate ad ogni punto del cluster
    # +++ dictFlat['nome_classe']= non mi ricordo in questo momento

    def cluster(self,dictImages,percentTest):
        dictCenter={}
        dictLabel={}
        dictFlat={}
        for j in dictImages.keys():
            listFlat=[]
            for i in range(len(dictImages[j])):
                result = dictImages[j][i].flatten()
                listFlat.append(result)
 
            kmeans = KMeans(n_clusters=(int(len(dictImages[j])*percentTest)), random_state=0).fit(listFlat)
            dictCenter[j]=kmeans.cluster_centers_
            dictLabel[j]= kmeans.labels_
            dictFlat[j]=listFlat

        return (dictCenter, dictLabel, dictFlat)


    #Per ogni classe divide i il test e il train utilizzando i dizionari utilizzati prima
    # E creo un iseme di indici che indicano il i punti più vicini ai centroidi
    # di ogni classe 
    def ImageIndex(self,dictImages,dictCenter,dictLabel,dictFlat):
        dictIndex={}
        for j in dictImages.keys():
            listIndex=[]
            for i in range(len(dictCenter[j])):
                min=math.inf
                index=0
                for z in range(len(dictFlat[j])):
                    #Qui devo calcolare la distanza euclidea perchè il centrodi prodotto dalla funzione precedente 
                    #è un punto sul piano che non corrisponde ad un punto effettivo.
                    #Per questo per ogni cluster cerco il punto con il centroide 
                    if(dictLabel[j][z]==i):
                        dst = distance.euclidean(dictCenter[j][i], dictFlat[j][z])
                        if(dst<min):
                            min=dst
                            index=z
                listIndex.append(index)
            dictIndex[j]=listIndex

        return dictIndex

    # In base all'index calcolato nel punto precedente faccio la divisione
    def spliTestTrain(self,setImages,dictIndex):

        test = {}
        images = {}


        for j in setImages.keys():
            listTest= [] 
            listTrain = []
            for i in range(len(setImages[j])):
                if(i in dictIndex[j]):
                    listTest.append(setImages[j][i])
                else:
                    listTrain.append(setImages[j][i])
            test[j]=listTest
            images[j]=listTrain

        return (test,images)


    def filter_image(self,setImage):
        gaussianBlurKernel = np.array(([[1, 2, 1], [2, 4, 2], [1, 2, 1]]), np.float32)/9
        sharpenKernel = np.array(([[0, -1, 0], [-1, 9, -1], [0, -1, 0]]), np.float32)/9
        meanBlurKernel = np.ones((3, 3), np.float32)/9

        setImages={}
        for j in setImage.keys():
            listClass=[]
 
            for i in range(len(setImage[j])):
    
                filter_image=cv2.filter2D(src=setImage[j][i], kernel=meanBlurKernel, ddepth=-4)
                listClass.append(filter_image)
 
    
    
            setImages[j]=listClass
        return setImages


    def SSE(self, dictFlat):
        dictSSE={}
        for j in dictFlat.keys():
            listFlat=dictFlat[j]
            kmeans = KMeans(n_clusters=(1), random_state=0).fit(listFlat)
            dictSSE[kmeans.inertia_]=j


        return dictSSE



    def remove_class(self, dictClass, filtered):

        dictIntraClassSSE.values()
        list1=[]
        list2=[]
        for j in dictIntraClassSSE.keys():
            list2.append(dictIntraClassSSE[j])
            list1.append(j)

            list1, list2 = zip(*sorted(zip(list1, list2)))

            lis=[]

        for i in range(10,25):
            lis.append(list2[i])

        for i in lis:
            del filtered[i]

        return filtered










