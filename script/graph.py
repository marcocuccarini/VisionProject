# -*- coding: utf-8 -*-
"""dsnlp-lib

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Sx1BQQtw9Ti1sReJYNc5aELVdcrh3Rys
"""

import sys
sys.path.append('/home/nbuser/library/')
import numpy as np
import cv2
import os
from scipy import ndimage
from scipy.spatial import distance
from sklearn.cluster import KMeans


class graph():
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


	def find_weidth_shortest_path(graph, start, end, path =[]):
		path = path + [start]
		if start == end:
			return path
		shortest = None
		for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
				if newpath:
					if not shortest or len(newpath) < len(shortest):
						shortest = newpath
		return shortest




	 