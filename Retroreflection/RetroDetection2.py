
import cv2 as cv
import numpy as np
from skimage import data, io, filters
#from time import sleep

#path = '/home/slewkowitz/MYTI/850/face.avi'
path = '/home/slewkowitz/MYTI/850/body.avi'

PATH2 = "/home/slewkowitz/GitRepo/Retroreflection/retroBodyCropPNG/"

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
    
    #image = image[:256,:256]
    print(image.shape)
    filename = PATH2 + "body" + str(i) + '.png'
    #cv.imwrite(filename, image)

# path = '/home/slewkowitz/GitRepo/retroFaces/face19.jpg'

# # image = cv.imread(path)

# image = cv.imread(path,cv.IMREAD_GRAYSCALE)
# edges = filters.sobel(image)
# # io.imshow(edges)
# # io.show()


# detector = cv.SimpleBlobDetector_create()

# # detector = cv.SimpleBlobDetector()

# # Detect blobs.
# keypoints = detector.detect(image)

# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Show keypoints
# cv.imshow("Keypoints", im_with_keypoints)