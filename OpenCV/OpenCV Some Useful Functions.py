import cv2
import numpy as np
kernel = np.ones((5,5), np.uint8)


img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\lena.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

imgCanny = cv2.Canny(img, 150, 200)

imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)   # Thicken the border of Canny image

imgEroded = cv2.erode(imgDialation, kernel, iterations = 1)   # Thin the border of Dialated image


cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dialated Image', imgDialation)
cv2.imshow('Eroded Image', imgEroded)


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break