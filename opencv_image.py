import cv2
img = cv2.imread('venv\pic1.jpeg',1)
#img= cv2.resize(img,(400,400))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
