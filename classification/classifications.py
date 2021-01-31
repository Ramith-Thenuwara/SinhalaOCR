# Image path, number of rows
# and number of columns
# should be provided as an arguments
import cv2
import sys
import os


if not os.path.exists('data/collection'):
    os.makedirs('data/collection')



nRows = int(sys.argv[2])
# Number of columns
mCols = int(sys.argv[3])

# Reading image
img = cv2.imread(sys.argv[1])
#print img

#cv2.imshow('image',img)

# Dimensions of the image
sizeX = img.shape[1]
sizeY = img.shape[0]

print(img.shape)


for i in range(0,nRows):
    for j in range(0, mCols):
        roi = img[i*sizeY/nRows:i*sizeY/nRows + sizeY/nRows ,j*sizeX/mCols:j*sizeX/mCols + sizeX/mCols]
        cv2.imshow('rois'+str(i)+str(j), roi)
        cv2.imwrite('data/collection_'+str(i)+str(j)+".jpg", roi)



cv2.waitKey()