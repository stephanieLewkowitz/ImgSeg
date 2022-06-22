
import cv2 as cv
import numpy as np
from time import sleep

path = '/home/slewkowitz/MYTI/850/body.avi'

fourcc = cv.VideoWriter_fourcc(*'XVID')
cap = cv.VideoCapture(path) 
i = 0
while(True):
    i = i+1
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is False:
        break

    image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    crop = image[:128,:]
    image2 = cv.resize(crop,[256,256])
    
    filename = "/home/slewkowitz/GitRepo/Retroreflection/retroBodyCrop/bodyCrop_" + str(i) + '.jpg'
    cv.imwrite(filename, image2)
    
   #  docker run --name cvat-server -v /home/slewkowitz/GitRepo:/home/django/data -d openvino/cvat_server

