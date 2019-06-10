import cv2 as cv
import numpy as np


def fill_color(img):  # 多通道
    copy_image = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)   # 一定单通道
    cv.floodFill(copy_image, mask, (30, 30),
                 (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('flood', copy_image)


def fill_binary():   # 单通道
    my_image = np.zeros((400, 400, 1), np.uint8)
    my_image[100:300, 100:300] = 255
    cv.imshow('my image', my_image)

    mask = np.ones((402, 402, 1), np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(my_image, mask, (200, 200), 100, cv.FLOODFILL_MASK_ONLY)
    cv.imshow('binary', my_image)


image = cv.imread('img0.jpg', 1)
fill_color(image)
fill_binary()
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()

