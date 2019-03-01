import cv2 as cv
import numpy as np

img = cv.imread(path)
normalizedImg = np.zeros((800, 800))
cv.normalize(img,  normalizedImg, 0, 255, cv.NORM_MINMAX)
cv.imshow('dst_rt', self.normalizedImg)
cv.waitKey(0)
cv.destroyAllWindows()
