import cv2 as cv
import numpy as np


def connect_component(img):
    src = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.namedWindow('binary', cv.WINDOW_AUTOSIZE)
    cv.imshow('binary', binary)

    # output = cv.connectedComponents(binary, connectivity=8)
    output = cv.connectedComponentsWithStats(binary, connectivity=8, ltype=cv.CV_32S)
    print(type(output))
    num_numbers = output[0]
    labels = output[1]
    status = output[2]
    centers = output[3]
    print(type(labels))
    print(labels.shape)
    print(num_numbers)
    colors = []
    for i in range(num_numbers):
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))

    colors[0] = (0, 0, 0)
    dst = np.zeros(src.shape, np.uint8)
    for row in range(gray.shape[0]):
        for col in range(gray.shape[1]):
            dst[row, col] = colors[labels[row, col]]

    for t in range(1, num_numbers, 1):
        x, y, w, h, area = status[t]
        cx, cy = centers[t]
        cv.circle(img, (np.int(cx), np.int(cy)), 1, (0, 255, 0), 2, 8, 0)
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0))
        # cv.putText(img, "num:"+str(t), (x, y), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, .5, (0, 0, 255), 1)

    cv.imshow('component', dst)
    cv.imshow('other', img)


image = cv.imread("E:/cvdata/bubble1.jpg")
print(image.shape)
cv.imshow('image', image)
connect_component(image)
cv.waitKey(0)
cv.destroyAllWindows()
