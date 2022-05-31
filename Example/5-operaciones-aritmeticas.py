import cv2
import numpy as np

image1 = cv2.imread('image/rick-and-morty-screaming-sun-1024x475.jpg.')
image2 = cv2.imread('image/rick-and-morty-unitys-planet-1024x475.jpg')


# suma
#weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
#cv2.imshow('Weighted Image', weightedSum)
#if cv2.waitKey(0) & 0xff == 27:
#    cv2.destroyAllWindows()

# resta
sub = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', sub)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
