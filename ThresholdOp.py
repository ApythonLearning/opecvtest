import cv2 as cv
import numpy as np


def threshold_demo(): # 整体二值化
    img = cv.imread('img0.jpg', 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # ret, dst = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # ret, dst = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # ret, dst = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
    print(ret)
    cv.imshow('binary', dst)


def local_threshold():  # 局部阈值化 自适应
    img = cv.imread('img0.jpg', 1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('binary', binary)


# threshold_demo()
local_threshold()
cv.waitKey(0)
cv.destroyAllWindows()





