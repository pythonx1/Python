import cv2
image = cv2.imread('nanana.jpg',0) 
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.line(img, (0,0),(511,511),(255,0,0),5)


