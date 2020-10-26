import cv2
import numpy as np


img = np.ones((520,520,3), np.uint8)   # images are nothing but matrix of pixels
img[:] = 200,200,200
img[200:300, 200:300] = 255,255,0    #{coloring the cropped zone}
#print(img)


cv2.line(img, (0,0), (300,300), (0,105,0), 5) 
cv2.rectangle(img, (0,520), (200,300), (100,100,50), cv2.FILLED)
cv2.circle(img, (450,50), 30, (155,155,0), 5)

cv2.putText(img, 'OpenCV', (300,200), cv2.FONT_HERSHEY_COMPLEX, 1, (150,150,50), 2)

cv2.imshow('Image', img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break