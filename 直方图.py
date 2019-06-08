import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def plot_demo(image):            # 直方图绘制
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show('histgram')


def eqhist(image):               # 直方图均衡化
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    cv.imshow('equalHist demo', gray)


def clahe_demo(image):   # 局部直方图均衡化 参数可调
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clahe', dst)


def create_rgb_hist(image):   #  三通道RGB直方图绘制
    histdata = np.zeros((16*16*16, 1), np.float32)
    (h, w, ch) = image.shape
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            (b, g, r) = image[row, col]
            index = np.int(b/bsize)*256+np.int(g/bsize)*16+np.int(r/bsize)
            histdata[np.int(index), 0] = histdata[np.int(index), 0]+1
    return histdata


def hist_compara(image1, image2):         #  直方图比较
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    compara1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    compara2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    compara3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴氏距离：%s 相关性：%s 卡方：%s'%(compara1, compara2, compara3))


if __name__ == '__main__':
    img = cv.imread('3.5.jpg', 1)
    print(img.shape)
    grayy = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(grayy.shape)
    plot_demo(img)
    cv.imshow('hist', img)
    eqhist(img)
    clahe_demo(img)

    img1 = cv.imread('img0.jpg', 1)
    img2 = cv.imread('3.5.jpg', 1)
    hist_compara(img1, img2)

    cv.waitKey(0)
    cv.destroyAllWindows()
