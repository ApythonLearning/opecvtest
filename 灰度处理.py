import cv2 as cv
import numpy as np


img = cv.imread('img0.jpg', 1)  # 0读取灰度图 1读取jpg  方法3
# dst = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 方法1
img_info = img.shape
print(img_info)
# print(dst.shape)
# cv.imshow('dst', dst)
height = img_info[0]
weight = img_info[1]

dst = np.zeros((height, weight, 3), np.uint8)
for i in range(height):
    for j in range(weight):
        (b, g, r) = img[i, j]
        gray = (int(b)+int(g)+int(r))/3
        dst[i, j] = np.uint(gray)

cv.imshow('gray', dst)
(b, g, r) = dst[100, 100]
print(b, g, r)  # 三个通道都为160
print(dst.shape)

cv.waitKey(0)
cv.destroyAllWindows()

