

import sys
sys.path.append('/home/nbuser/library/')
import numpy as np
import cv2
import os
from scipy import ndimage
from scipy.spatial import distance
from sklearn.cluster import KMeans



class graph():

	def findedges1(self, start, end, path =[]):
		path = path + [start]
		print(path)
		if start == end:
			return path
		shortest=None
		for node in self.gdict:
			if node not in path:
				newpath = self.findedges1(node, end, path)

				if newpath:
					if not shortest or len(newpath) < len(shortest):
						shortest = newpath
						print(shortest)

		
		return shortest



	def __init__(self,gdict=None):
		if gdict is None:
			gdict = {}
		self.gdict = gdict

	def edges(self):
		return self.findedges()

	def AddEdge(self, edge):
		edge = set(edge)
		(vrtx1, vrtx2) = tuple(edge)
		if vrtx1 in self.gdict:
			self.gdict[vrtx1].append(vrtx2)
		else:
			self.gdict[vrtx1] = [vrtx2]

	def findedges(self):
		edgename = []
		for vrtx in self.gdict:
			for nxtvrtx in self.gdict[vrtx]:
				if {nxtvrtx, vrtx} not in edgename:
					edgename.append({vrtx, nxtvrtx})
		return edgename


	




	 