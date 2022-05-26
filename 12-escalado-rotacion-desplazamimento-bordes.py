import cv2
import numpy as np


FILE_NAME = 'image\cat.jpg'

# escalado de imagen
# try:
#     img = cv2.imread(FILE_NAME)
#     (height, width) = img.shape[:2]
#     res = cv2.resize(img, (int(width / 2), int(height / 2)),
#                      interpolation=cv2.INTER_CUBIC)
#     cv2.imwrite('resultado-escala.jpg', res)
# except IOError:
#     print('Error while reading files !!!')

# Rotación de una imagen
try: 
    img = cv2.imread(FILE_NAME)
    (rows, cols) = img.shape[:2] 
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1) 
    res = cv2.warpAffine(img, M,(cols, rows)) 
    cv2.imwrite('resultado-rotacion.jpg', res) 
except IOError: 
    print ('Error while reading files !!!') 

