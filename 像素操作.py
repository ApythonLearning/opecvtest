import cv2 as cv

img = cv.imread("F:/code/timg.jpg", 1)

(b, g, r) = img[100, 100]
print(b, g, r)

#  像素的写入
for i in range(100):
    img[100, 100+i] = (255, 0, 0)

cv.namedWindow('test', 1)
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()