#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:39:23 2021

@author: doreen
"""
# corner.py
import cv2 as cv

def blob(path="/Users/doreen/Desktop/project/234.jpg"):
    
    frame = cv.imread(path)
    #cv.imshow("input", frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    params = cv.SimpleBlobDetector_Params()

    # change thresholds閾值控制
    params.minThreshold = 0
    params.maxThreshold = 256
    
    params.filterByColor = True
    params.blobColor =0
    
    # filter by area像素面積大小控制
    params.filterByArea = True
    params.minArea = 22
    params.maxArea = 5000
    
    # Filter by Inertia形狀（園）
    params.filterByCircularity = True
    params.minCircularity = 0.1
    
    # filter by circularity形狀（凸）
    params.filterByConvexity = True
    params.minConvexity = 0.5
    
    # Filter by Convexity形狀（凹）
    params.filterByInertia = True
    params.minInertiaRatio = 0.5
    
    # 提取关键点
    detector = cv.SimpleBlobDetector_create(params)
    keypoints = detector.detect(gray)
    number = 0
    for marker in keypoints:
        result = cv.drawMarker(frame, tuple(int(i) for i in marker.pt), color=(255, 0, 0))
        number = number + 1
        
    return number
'''
用這個測試
if __name__ == '__main__':
   ans =  blob()
   print(ans)
'''

'''    
print("斑點數量：")
print(number)
if number <= 0:
    print("point:0")
elif number > 0 and number <= 10:
    print("point:50")
else:
    print("point:100")
cv.imshow("result", result)
cv.waitKey(0)
cv.destroyAllWindows()
'''

