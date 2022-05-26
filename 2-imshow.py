import cv2

# El método cv2.imshow() se utiliza para mostrar una
# imagen en una ventana. La ventana se ajusta automáticamente
# al tamaño de la imagen.

""" path = r'image/perro.jpg'
image = cv2.imread(path) 
window_name = 'image'
cv2.imshow(window_name, image) 
cv2.waitKey(0)  
cv2.destroyAllWindows()   """

path = r'image/perro.jpg'
image = cv2.imread(path, 0) 
window_name = 'image'
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 