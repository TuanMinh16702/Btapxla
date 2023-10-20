import cv2

img = cv2.imread("img/lena512color.jpg")

img2 = 255 - img
cv2.imshow("ảnh gốc", img)
cv2.imshow("Ảnh sau khi chỉnh", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img/lena_negative.jpg", img2)