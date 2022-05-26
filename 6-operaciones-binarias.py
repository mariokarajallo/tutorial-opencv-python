# Las operaciones bit a bit se utilizan en la manipulación de imágenes y se utilizan para extraer partes esenciales de la imagen.

import cv2
import numpy as np

image1 = cv2.imread('input1.jpg')
image2 = cv2.imread('input2.jpg')

dest_and = cv2.bitwise_and(img2, img1, mask=None)

cv2.imshow('Bitwise And', dest_and)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
