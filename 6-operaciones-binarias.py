# Las operaciones bit a bit se utilizan en la manipulación de imágenes y se utilizan para extraer partes esenciales de la imagen.

import cv2
import numpy as np

image1 = cv2.imread('image\square.jpg')
image2 = cv2.imread('image\circle.jpg')

# operacion AND
""" dest_and = cv2.bitwise_and(image2, image1, mask=None)
cv2.imshow('Bitwise And', dest_and)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows() """

# operacion OR
dest_or = cv2.bitwise_or(image2, image1, mask=None)
cv2.imshow('Bitwise OR', dest_or)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
