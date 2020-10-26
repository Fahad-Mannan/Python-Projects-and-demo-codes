import cv2


def empty(a):
    pass


img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\Lena.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 640, 100)
cv2.createTrackbar('canny1', 'Trackbar', 173, 300, empty)
cv2.createTrackbar('canny2', 'Trackbar', 65, 300, empty)

while True:
    canny1 = cv2.getTrackbarPos('canny1', 'Trackbar')
    canny2 = cv2.getTrackbarPos('canny2', 'Trackbar')

    canny = cv2.Canny(gray, canny1, canny2)

    cv2.imshow('Img', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
