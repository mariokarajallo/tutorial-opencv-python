# Python program to explain cv2.cvtColor() method

# importing cv2
import cv2

# # path
# path = r'image/perro.jpg'

# # Reading an image in default mode
# src = cv2.imread(path)

# # Window name in which image is displayed
# window_name = 'Image'

# # Using cv2.cvtColor() method
# # Using cv2.COLOR_BGR2GRAY color space
# # conversion code
# image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )

# # Displaying the image
# cv2.imshow(window_name, image)



#EJEMPLO 2
# Uso del espacio de color HSV. El espacio de color HSV se utiliza principalmente para
# el seguimiento de objetos.

# path
path = r'image/cat.jpg'

# Reading an image in default mode
src = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )

# Displaying the image
cv2.imshow(window_name, image)












# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()