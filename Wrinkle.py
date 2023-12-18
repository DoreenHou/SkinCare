#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:27:38 2021

@author: doreen
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display, Image

def wrinkle(path1="/Users/doreen/opt/anaconda3/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml", 
            path2="/Users/doreen/Desktop/Wrinkles-Detection-master/images.jpg"):
    number_of_edges = 0
    #creating facecascade
    face_cascade = cv2.CascadeClassifier(path1)
    #display(Image(filename='/Users/doreen/Desktop/Wrinkles-Detection-master/images.jpg'))
    #loading image to matrix
    img = cv2.imread(path2)

    #converting into grayscale image
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05,minNeighbors=10)
    for x,y,w,h in faces : 
        cropped_img = img[y:y+h,x:x+w]
        edges = cv2.Canny(cropped_img,100,800)        
        number_of_edges = np.count_nonzero(edges)
    return number_of_edges
'''
if __name__ == '__main__':
   ans =  wrinkle()
   print(ans)
'''
'''
if number_of_edges > 500 and number_of_edges <= 800:
    print("point:100 ")
elif number_of_edges > 800:
    print("point:50")
else:
    print("point:30")
'''
