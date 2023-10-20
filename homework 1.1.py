import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("img/moon.jpg",cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit= 2.0, tileGridSize = (8,8))
cl = clahe.apply(img)

plt.figure(figsize = (10,8))
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("Original")

plt.subplot(2,2,2)
plt.imshow(cl,cmap='gray')
plt.title("After ")

histogram_ori = cv2.calcHist([img],[0],None,[256],[0,256])
plt.subplot(2,2,3)
plt.bar(np.arange(256),histogram_ori.ravel())
plt.xlim([0,255])
plt.title("Ori Histogram")

histogram_ori = cv2.calcHist([cl],[0],None,[256],[0,256])
plt.subplot(2,2,4)
plt.bar(np.arange(256),histogram_ori.ravel())
plt.xlim([0,255])
plt.title("After Histogram")

plt.show()



cv2.waitKey()