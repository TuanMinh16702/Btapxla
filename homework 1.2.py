import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure,io
import cv2

img = cv2.imread('img/skull.jpg',cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.imshow(img, cmap= 'gray')
plt.title('Hình gốc')

eqImg = cv2.equalizeHist(img)
plt.subplot(2,2,2)
plt.imshow(eqImg, cmap = 'gray')
plt.title('Cân bằng biểu đồ toàn cầu')

ahe_img = exposure.equalize_adapthist(img,kernel_size = (8,8))
plt.subplot(2,2,3)
plt.imshow(ahe_img, cmap='gray')
plt.title('Cân bằng biểu đồ 8x8 thích ứng')

ahe_img = exposure.equalize_adapthist(img,kernel_size = (16,16))
plt.subplot(2,2,4)
plt.imshow(ahe_img, cmap='gray')
plt.title('Cân bằng biểu đồ 16x16 thích ứng')

plt.show()

