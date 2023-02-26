import cv2

# Leer imagen
img = cv2.imread("butterfly.jpg")

# Mostrar imagen a color
cv2.imshow()

# Convertir imágenes a color en escala de grises
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Mostrar imagen en escala de grises
cv2.imshow()


#print(gray_img)

cv2.waitKey(0)