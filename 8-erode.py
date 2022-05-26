import cv2
import numpy as np

path = r'image/perro.jpg'
image = cv2.imread(path)
window_name = 'Image'

#ejemplo 1
# kernel = np.ones((5, 5), np.uint8)
# image = cv2.erode(image, kernel)
# cv2.imshow(window_name, image)
# cv2.waitKey(0)

#ejemplo 2
kernel = np.ones((5, 5), np.uint8)
image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)
cv2.imshow(window_name, image)
cv2.waitKey(0)
