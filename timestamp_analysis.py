import cv2
import matplotlib.pyplot as plt
import os
import time
import numpy as np
from os.path import isfile, join

class compare_timestamps(object):
    def __init__(self, file_path_to_timestamps,fps, dataframe_camera, dataframe_velodyne, *args):
        self.file_path_to_timestamps = file_path_to_timestamps
        self.__image = __image
        self.fps = fps
        self.dataframe_camera = dataframe_camera
		self.dataframe_velodyne = dataframe_velodyne
       
    def convert_frames_to_video(self, pathIn,pathOut,fps):
        frame_array = []
        files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
        #for sorting the file names properly
        files.sort(key = lambda x: int(x[5:-4]))
 
        for i in range(len(files)):
            filename = pathIn + files[i]
            #reading each files
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            print(filename)
            #inserting the frames into an image array
            frame_array.append(img)
 
        out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
        for i in range(len(frame_array)):
            # writing to a image array
            out.write(frame_array[i])
        out.release() 

    def time_stamp_parsing(self, time_stamp_file_path, dataframe_camera, dataframe2):
		dataframe_camera = pd.read_table(time_stamp_file_path)
		df['date'], df['timestamps'] = df['2011-09-26 13:02:25.445761280'].str.split(' ', 1).str