import cv2
img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\logo.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img, contours, -1, (255,255,0), 2)


print('Number of contours' + str(len(contours)))
print(contours[0])

cv2.imshow('Image', img)
#cv2.imshow('ImageGray', imgGray)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break