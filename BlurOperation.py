import cv2 as cv
import numpy as np


def hold_value(vla):   # 防止噪声越界
    if vla > 255:
        return 255
    elif vla < 0:
        return 0
    else:
        return vla


def customer_blur(image):  # 自定义模糊  效果接近 均值模糊blur
    kernel = np.ones((5, 5), np.float32)/25  # 保证不会溢出
    blur = cv.filter2D(image, -1, kernel)
    cv.imshow('DIY blur', blur)


def gaussian_noise(image):   # 高斯噪声
    h, w, ch = image.shape
    for i in range(h):
        for j in range(w):
            s = np.random.normal(0, 20, 3)
            (b, g, r) = image[i, j]
            image[i, j] = (hold_value(b+s[0]), hold_value(g+s[1]), hold_value(r+s[2]))  # hold_value 防止数据越界
    cv.imshow('guassian_noise', image)
    return image


def bilateral_blur(image):               #  双边模糊
    b_b_demo = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow('bilateral blur', b_b_demo)


t1 = cv.getTickCount()
img = cv.imread('img0.jpg', 1)
dst = cv.medianBlur(img, 5)
cv.imshow('m', img)
cv.imshow('blur', dst)
customer_blur(img)
gaussian_noise_demo = gaussian_noise(img)
cv.imshow('gaussianBlur', cv.GaussianBlur(gaussian_noise_demo, (0, 0), 10))  # 高斯模糊
t2 = cv.getTickCount()
time = ((t2 - t1)/cv.getTickFrequency())*1000
print('time is '+str(time))
bilateral_blur(img)
cv.waitKey(0)
cv.destroyAllWindows()
