import cv2 as cv
import numpy as np


def threshold_demo(image):
    image = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    return binary


def canny_demo(image):
    t = 80
    canny_output = cv.Canny(image, t, t*2)
    cv.imshow('canny', canny_output)
    return canny_output


# src = cv.imread('E:/cvdata/bubble1.jpg')
src = cv.imread('E:/cvdata/stuff.jpg')
cv.imshow('image', src)
dst = threshold_demo(src)
binary = canny_demo(src)
k = np.ones((3, 3), np.uint8)
binary = cv.morphologyEx(binary, cv.MORPH_DILATE, k)
cv.imshow('binary', binary)

out, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# out, contours, hierarchy = cv.findContours(dst, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(type(contours), type(hierarchy))
for c in range(len(contours)):
    # cv.drawContours(src, contours, c, (0, 255, 0))
    # x, y, w, h = cv.boundingRect(contours[c])
    # cv.rectangle(src, (x, y), (x+w, y+h), (0, 255, 0), 1, 8, 0)
    rect = cv.minAreaRect(contours[c])  # 返回最小外接矩形 中心点位置 矩形宽高 旋转角度
    # print(type(rect))
    cx, cy = rect[0]
    box = cv.boxPoints(rect)
    # print(type(box))
    box = np.int0(box)
    cv.drawContours(src, [box], 0, (255, 0, 0), 2)
    cv.circle(src, (np.int32(cx), np.int32(cy)), 2, (0, 255, 0), 2, 8, 0)


cv.imshow('minarea', src)
cv.waitKey(0)
cv.destroyAllWindows()
