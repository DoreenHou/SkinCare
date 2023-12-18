#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 21:13:00 2021

@author: doreen
"""

import cv2
import numpy as np

def redness(path="D:/face3.jpg"):
    
    img = cv2.imread(path)
    # range of red
    lower_red = np.array([160, 60, 60])
    upper_red = np.array([180, 255, 255])

    lower_red2 = np.array([0, 60, 60])
    upper_red2 = np.array([10, 255, 255])  # thers is two ranges of red
    
    # range of yellow
    # lower_yellow = np.array([10,100,100])
    # upper_yellow = np.array([45,255,255])
    
    # range of grenn
    # lower_yellow = np.array([36,25,25])
    # upper_yellow = np.array([70,255,255])
    
    # change to hsv model
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    mask_r = cv2.inRange(hsv, lower_red, upper_red)
    
    mask_r2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = mask_r + mask_r2
    
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    mask = cv2.dilate(mask, kernel)
    x,y = mask.shape
    total = x*y
    
    good = np.sum(mask==0)
    bad = np.sum(mask==255)
    
    precent = bad/total
    
    return precent   

'''
if __name__ == '__main__':
   ans =  redness()
   print(ans)
'''   
   
   
   
                          