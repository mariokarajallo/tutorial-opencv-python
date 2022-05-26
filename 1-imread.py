import cv2
#Para leer las imágenes se utiliza el método cv2.imread().
# Este método carga una imagen del archivo especificado.
# Si la imagen no se puede leer(debido a que falta un archivo,
# permisos inadecuados, formato no compatible o no válido),
# este método devuelve una matriz vacía.

""" img = cv2.imread("image/perro.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Cute Kitens", img)
cv2.waitKey(0)
cv2.destroyAllWindows() """

#escala de gris
path = r'image/perro.jpg'
img = cv2.imread(path, 0) 
cv2.imshow('image', img)
cv2.waitKey(0)

