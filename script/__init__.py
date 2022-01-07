
import sys
sys.path.append('/home/nbuser/library/')
import numpy as np
from numpy import savetxt
from numpy import asarray

from numpy import loadtxt
import cv2
import os
from scipy import ndimage
from scipy.spatial import distance
from sklearn.cluster import KMeans
from .graph import *
from .preprocessing import *
from .input_data import *
from .utility import *
from .spatial_pyramid import *


class BagofWord():

	#def __init__(self):
    	# upload of data in a dictionary
		def load_images_from_folder(self, folder):
		    images = {}
		    
		    for filename in os.listdir(folder):
		        category = []
		        path = folder + "/" + filename
		        for cat in os.listdir(path):
		        	#load each image with a gray scale 
		            img = cv2.imread(path + "/" + cat, 0)
		            #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		            if img is not None:
		                category.append(img)
		        images[filename] = category
		        
		    return images

		    #Estraggo le sift_features
		def sift_features(self, images):
			sift_vectors = {}
			descriptor_list = []
			sift = cv2.SIFT_create()
			for key,value in images.items():
				features = []
				for img in value:
					kp, des = sift.detectAndCompute(img,None)
			           
			            
					descriptor_list.extend(des)
					features.append(des)
				sift_vectors[key] = features
			return [descriptor_list, sift_vectors]

        #restituisce i centroidi creati per la creazione 
        # di 10 cluster (numero delle classi)
		def kmeans(self, k, descriptor_list):

				kmeans = KMeans(n_clusters = k, n_init=10)
				kmeans.fit(descriptor_list)
				visual_words = kmeans.cluster_centers_ 
				return visual_words

		
		#Trova la label più vicina per ogni classe:
		#(questo momento mi è venuto in mente che si può provare a fare un pò di modifica.)
		def find_index(self, image, center):
				count = 0
				ind = 0
				for i in range(len(center)):
						if(i == 0):
								count = distance.euclidean(image, center[i])
								#count = L1_dist(image, center[i])
	           
						else:
								dist = distance.euclidean(image, center[i])
								#dist = L1_dist(image, center[i])
								



								if(dist < count):
										nd = i
										count = dist



				return ind


		'''def find_index(self, img, center):

			dictIndex={}
			l=[]

			
			for c in range(len(center)):



				dictIndex[c]=l



			for image in img:

				for c in range(len(center)):

					y=dictIndex[c]
					y.append(distance.euclidean(image, center[c]))
					dictIndex[c]=y


			for i in dictIndex.keys():

				dictIndex[i]=dictIndex[i].sort()


			return dictIndex'''




		def image_class(self, all_bovw, centers):
			    dict_feature = {}
			    for key,value in all_bovw.items():
			        category = []
			        for img in value:
			            histogram = np.zeros(len(centers))

			            for each_features in img:

			            #lIndex=self.getDictIndex(img, centers)
			            	ind = self.find_index(each_features, centers)
			            	histogram[ind] += 1


			            category.append(histogram)
			        dict_feature[key] = category
			    return dict_feature


		def knn(self, images, tests):
		    num_test = 0
		    correct_predict = 0
		    class_based = {}
		    listKey=[]
		    listTestKey=[]
		    
		    for test_key, test_val in tests.items():
		        class_based[test_key] = [0, 0] # [correct, all]
		        for tst in test_val:
		            predict_start = 0
		            #print(test_key)
		            minimum = 0
		            key = "a" #predicted
		            for train_key, train_val in images.items():
		                for train in train_val:
		                    if(predict_start == 0):
		                        minimum = distance.euclidean(tst, train)
		                        #minimum = L1_dist(tst,train)
		                        key = train_key
		                        predict_start += 1
		                    else:
		                        dist = distance.euclidean(tst, train)
		                        #dist = L1_dist(tst,train)
		                        if(dist < minimum):
		                            minimum = dist
		                            key = train_key

		            
		            listKey.append(key)
		            listTestKey.append(test_key)
		            
		            
		    return [listKey,listTestKey]

		



	 