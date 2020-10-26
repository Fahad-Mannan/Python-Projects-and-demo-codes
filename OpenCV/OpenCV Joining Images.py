import cv2
import numpy as np

img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\joker_warped.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgHorizontal = np.hstack((img,img,img))

imgVertical = np.vstack((img,img))

cv2.imshow('Horizontal Image', imgHorizontal)
cv2.imshow('Vertical Image', imgVertical)


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break 