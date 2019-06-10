import cv2 as cv
import numpy as np


def canny_demo():
    img = cv.imread('img0.jpg', 1)
    cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
    cv.imshow('img', img)
    img_info = img.shape
    height = img_info[0]
    width = img_info[1]
    dst = np.zeros((height, width, 3), np.uint8)
    #  gray -> guss -> canny
    dst = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    dst = cv.GaussianBlur(dst, (3, 3), 0)
    canny = cv.Canny(dst, 50, 100)
    cv.imshow('canny', canny)




canny_demo()
cv.waitKey(0)
cv.destroyAllWindows()

