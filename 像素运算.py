import cv2 as cv
import numpy as np


class ClImage:
    def __init__(self, img, dst):
        self.img = img
        self.dst = dst
        cv.imshow('img', self.img)
        cv.imshow('dst', self.dst)

    def add_img(self):
        ad = cv.add(self.img, self.dst)
        cv.namedWindow('add', cv.WINDOW_AUTOSIZE)
        cv.imshow('add', ad)

    def sub_img(self):
        sub = cv.subtract(self.dst, self.img)
        cv.imshow('sub', sub)

    def other_op(self):
        mean1, stdv1 = cv.meanStdDev(self.img)  # 均值方差
        print(mean1, stdv1)

    def logi_demo(self):
        logic = cv.bitwise_and(self.img, self.dst)
        # logic = cv.bitwise_or()
        # logic = cv.bitwise_not()
        cv.namedWindow('logical', cv.WINDOW_AUTOSIZE)
        cv.imshow('logical', logic)

    def contrast_brightness_demo(self, c, b):  # 亮度b 对比度c
        h, w, ch = self.img.shape
        blank = np.zeros((h, w, ch), self.img.dtype)
        out = cv.addWeighted(self.img, c, blank, 1-c, b)
        cv.imshow('ContrastAndBright', out)


if __name__ == '__main__':
    m1 = cv.imread('WindowsLogo.jpg', 1)
    m2 = cv.imread('LinuxLogo.jpg', 1)
    demo = ClImage(m1, m2)
    image1_info = m1.shape
    image2_info = m2.shape
    print(image1_info)
    print(image2_info)
    demo.add_img()
    demo.sub_img()
    demo.other_op()
    demo.logi_demo()
    demo.contrast_brightness_demo(1.5, 0)
    cv.waitKey(0)
    cv.destroyAllWindows()
