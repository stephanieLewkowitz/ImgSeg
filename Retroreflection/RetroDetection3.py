import cv2 as cv
import numpy as np
from skimage import feature, io #pip install scikit-image
from time import sleep
import matplotlib.pyplot as plt

path = '/home/slewkowitz/MYTI/850/face.avi'

path2 = '/home/slewkowitz/GitRepo/retroFaces/face19.jpg'

# image = cv.imread(path)

image = cv.imread(path2,cv.IMREAD_GRAYSCALE)

fourcc = cv.VideoWriter_fourcc(*'XVID')
cap = cv.VideoCapture(path) 
i=0
while(True):
    i = i + 1
    if i == 19:
        print("check edges")
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret is False:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #output_image = np.zeros((512, 1024))#, np.uint8
    #output_image[0:256, 0:256] = gray

    
    edges1 = feature.canny(gray)
    y = edges1.astype(int)
   
    #output_image[0:256, 256:512] = y

    #_, thresh_eq_hist_img = cv.threshold(equilized_historgram_img, 170, 255, 0)
    #output_image[256:512, 256:512] = thresh_eq_hist_img

    #circles_img = np.zeros((256, 256), np.uint8)
    #circles = cv.HoughCircles(thresh_eq_hist_img, cv.HOUGH_GRADIENT, 1.2, 100) # Search for the circles in image (this doesn't work)
    #if circles is not None:
	#    circles = np.round(circles[0, :]).astype("int")
	 #   for (x, y, r) in circles:
	#	    cv.circle(circles_img, (x, y), r, (0, 255, 0), 4)
	#	    cv.rectangle(circles_img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    #output_image[256:512, 0:256] = circles_img

    #contours, hierarchy = cv.findContours(thresh_eq_hist_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cnt_img = np.zeros((256, 256), np.uint8)
    #cv.drawContours(cnt_img, contours, -1, (255), 2)
    #output_image[256:512, 512:768] = cnt_img

    if ret == True:
        plt.imshow(y)
       # cv.imshow('out', output_image)
       #cv.imshow('out', y)
       #io.imshow(y)

    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    sleep(0.15)

cap.release()
cv.destroyAllWindows()
