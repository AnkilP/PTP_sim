import cv2
import matplotlib.pyplot as plt
import os
import time
import numpy as np
from os.path import isfile, join
import pandas as pd

class timestamps(object):

	fps = 25

    def __init__(self, pathIn, *args):
        self.pathIn = pathIn
		self.values

	def time_stamp_parsing(self, time_stamp_file_path, df):
		df = pd.read_table(time_stamp_file_path, header= None)
		df['date'], df['timestamps'] = df[0].str.split(' ', 1).str
		df = df.drop(0, 1)
		self.values = pd.to_timedelta(df['timestamps'], unit = 's')
		return 0

class time_stamp_pairs(timestamps):



class timestamps_comparison(time_stamp_pairs):

	def __init__(self, *args):
		#stuff I need

	def greedy_algorithm(self, timestamps1, timestamps2, *args):
		index_matched_points = []
		i = 0
		#for i in range(len(timestamps_camera)): #slower one on top
		while i < len(timestamps_camera):
			#for j in range(timestamps_camera): #faster one at the bottom
			indexe = [0,0]
			j = 0
        
			while(timestamps_velodyne[j] >= timestamps_camera[i]):
				indexe[0] = timestamps_velodyne[i]
				indexe[1] = timestamps_camera[j]
				i = i + 1
				print("lets see what happens now")
			j = j+1
			index_matched_points.append(indexe)
			#indexe = [0,0]
		return index_matched_points