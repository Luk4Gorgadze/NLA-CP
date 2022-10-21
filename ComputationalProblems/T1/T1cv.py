import cv2 as cv
import numpy as np

def blend(a,b,alpha,maxLen,maxWid,c):
    pxlA = []
    pxlB = []
    
    for row in range(maxLen):
        for column in range(maxWid):
            pxlA = a[row][column]
            pxlB = b[row][column]
            c[row][column] =  pxlA * alpha + pxlB * (1-alpha)
    return c


Alpha = 0
a = cv.imread('ComputationalProblems/T1/imgs/dragon.jpg')
b = cv.imread('ComputationalProblems/T1/imgs/chameleon.jpg')  
maxLen = min(a.shape[0],b.shape[0])
maxWid = min(a.shape[1],b.shape[1]) 
c = np.zeros((maxLen,maxWid,3))
while Alpha < 1:
    c = blend(a,b,Alpha,maxLen,maxWid,c)
    cv.imshow("Video",c.astype(np.uint8))
    Alpha += .1
    cv.waitKey(1000)




