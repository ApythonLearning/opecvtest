import cv2 as cv
import numpy as np
'''
numpy数组操作
array = np.random.randn(3, 4)*10
c = array.flat
print(c)
for i in c:
    print(i)
print(len(array))  =3数组的行数 第一维长度

for i in range(10, -1, -1):   负数步长-1 应该从大到小 10 ....0
    print(i)
'''


def pyramid_down(pyramid_image, level=3):
    expand = pyramid_image
    for i in range(level-1, -1, -1):
        expand = cv.pyrUp(expand)
        cv.imshow('pyramid_down'+str(i), expand)


img = cv.imread('img0.jpg', 1)
cv.imshow('image', img)
# expand = cv.pyrUp(img)
# cv.imshow('pyramid', expand)
pyramid_down(img)

cv.waitKey(0)
cv.destroyAllWindows()
