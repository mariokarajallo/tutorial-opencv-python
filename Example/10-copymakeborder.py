import cv2

path = r'image/perro.jpg'

image = cv2.imread(path)

window_name = 'Image'
image = cv2.copyMakeBorder(image, 50, 10, 10, 10, cv2.BORDER_WRAP)
cv2.imshow(window_name, image)
cv2.waitKey(0)
