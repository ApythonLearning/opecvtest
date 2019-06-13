import cv2 as cv
import numpy as np

'''
图像卷积操作主要有三种功能：图像的模糊去噪，图像梯度/边缘的发现，图像锐化/增强
图像锐化的本质：图像拉普拉斯滤波加原图权重像素叠加的输出
[[-1 , -1, -1]
 [-1, C, -1]
 [-1 , -1, -1]
]
当C值大于8时表示图像锐化，越接近8表示锐化效果越好
当C等于8时图像的高通滤波
C值越大，图像的锐化效果在减弱，中心像素的作用在提升
'''

src = cv.imread('img0.jpg', 1)
cv.imshow('src', src)
# sharp_op = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32)
sharp_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
sharpen_image = cv.filter2D(src, cv.CV_32F, sharp_op)
sharpen_image = cv.convertScaleAbs(sharpen_image)
cv.imshow('sharpen', sharpen_image)

h, w = src.shape[:2]
dst = np.zeros([h, w*2, 3], src.dtype)
dst[:h, 0:w, :] = src
dst[:h, w:, :] = sharpen_image
cv.putText(dst, "original image", (10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.putText(dst, "sharpen image", (w+10, 30), cv.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv.imshow('result', dst)
cv.waitKey(0)
cv.destroyAllWindows()
