import cv2
import numpy as np

image = cv2.imread('image/fruits.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)

#desenfoque gausiano
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

#desenfoque mediano
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median)
cv2.waitKey(0)

#desenfoque bilateral
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()