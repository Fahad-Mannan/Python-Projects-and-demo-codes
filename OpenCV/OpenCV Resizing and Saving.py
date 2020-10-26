import cv2
import numpy as np

img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\jitu.jpg")
print(img.shape)

imgResize = cv2.resize(img, (540,675))
print(imgResize.shape)


cv2.imshow('Image', img)
cv2.imshow('Resized Image', imgResize)

cv2.imwrite(r"D:\Academia\Fahad's Projects\OpenCV\jitu_resized.jpg", imgResize)     #saving Image

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break