import numpy as np
import matplotlib.pyplot as plt
import cv2

M = cv2.imread("img/lena512color.jpg")

cv2.imshow("", M)
cv2.waitKey(0)
cv2.destroyAllWindows()

M1 = M.copy()
M1[:, :, 0] = M[:, :, 2]
M1[:, :, 1] = M[:, :, 0]
M1[:, :, 2] = M[:, :, 1]

cv2.imshow("Original Image", M)
cv2.imshow("J2 - Swapped Image", M1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img/lena512color_swapped.jpg", M1)