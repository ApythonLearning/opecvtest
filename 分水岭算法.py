import cv2 as cv
import numpy as np

'''
基于距离的分水岭分割流程：
输入图像->灰度->二值->距离变换->寻找种子->生成marker->分水岭变换->输出图像

'''


def washed_demo(image):
    print(image.shape)
    blur = cv.pyrMeanShiftFiltering(image, 10, 100)
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary', binary)

    # morph_op
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sur_bg = cv.dilate(opening, kernel, iterations=3)
    cv.imshow('background', sur_bg)

    # distance_transform
    dist_trans = cv.distanceTransform(opening, 1, 5)  # 0-CV_DIS_L1 1-CV_DIS_L2 2-CV_DIS_C
    ret, sur_fg = cv.threshold(dist_trans, 0.7*dist_trans.max(), 255, cv.THRESH_BINARY)

    # finding unknown region
    sur_fg = np.uint8(sur_fg)
    cv.imshow('foreGround', sur_fg)
    unknown = cv.subtract(sur_bg, sur_fg)
    cv.imshow('un', unknown)

    ret, markers = cv.connectedComponents(sur_fg)
    print(ret)

    # watershed transform
    markers = markers+1
    markers[unknown==255] = 0
    markers = cv.watershed(image, markers)
    image[markers == -1] = [0, 0, 255]
    cv.imshow('markers', markers)
    cv.imshow('watershed', image)


def run():
    img = cv.imread('circle.png', 1)
    cv.imshow('image', img)
    washed_demo(img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    run()

