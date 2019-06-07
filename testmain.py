import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)   # 左右变换1 上下-1
        cv.imshow('vedio', frame)
        c = cv.waitKey(10)
        if c == 27:
            break


def get_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pix_data = np.array(image)
    print(pix_data)


src = cv.imread('F:/code/timg.jpg', 1)
get_info(src)
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
