import cv2 as cv
import numpy as np


def sobel_demo(image):
    grade_x = cv.Sobel(image, cv.CV_32F, 1, 0)       #  cv.Scharr() soble的增强版
    grade_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradex = cv.convertScaleAbs(grade_x)
    gradey = cv.convertScaleAbs(grade_y)

    gradexy = cv.addWeighted(gradex, 0.5, gradey, 0.5, 0)

    cv.imshow('soble', gradexy)


def laplace_demo(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lap = cv.convertScaleAbs(dst, None)
    cv.imshow('laplace', lap)


def filter_lap(image):   # 使用卷积实现拉普拉斯算子
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('diy laplace', lpls)


img = cv.imread('img0.jpg', 1)
sobel_demo(img)
laplace_demo(img)
filter_lap(img)

cv.waitKey(0)
cv.destroyAllWindows()
