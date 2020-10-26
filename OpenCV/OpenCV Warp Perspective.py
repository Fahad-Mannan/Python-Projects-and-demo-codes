import cv2
import numpy as np

img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\joker.jpg")

width, height = 250, 350

pts1 = np.float32([[225, 93], [431, 138], [164, 383], [370, 425]])    # I got these point by openning the image in paint of my windows 7
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgWarped = cv2.warpPerspective(img, matrix, (width, height))
cv2.imwrite(r"D:\Academia\Fahad's Projects\OpenCV\joker_warped.jpg", imgWarped)

cv2.imshow('Image', img)
cv2.imshow('Warped Image', imgWarped)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
