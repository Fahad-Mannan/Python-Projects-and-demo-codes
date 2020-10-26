import cv2

img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\triangle.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgDil = cv2.dilate(imgCanny, (5, 5), iterations=3)
# ret, thresh = cv2.threshold(imgDil, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    if cv2.contourArea(contour) > 1000:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        print(len(approx))

        x, y, w, h = cv2.boundingRect(contour)
        cv2.putText(img, 'Points: ' + str(len(approx)), (x, y + 50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

        if len(approx) == 3:
            cv2.putText(img, 'Triangle', (x, y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
        if len(approx) == 4 and w != h:
            cv2.putText(img, 'Rectangle', (x, y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
        if len(approx) == 4 and w == h:
            cv2.putText(img, 'Square', (x, y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
        if len(approx) > 4:
            cv2.putText(img, 'Polygon', (x, y + 15), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow('Image', img)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break