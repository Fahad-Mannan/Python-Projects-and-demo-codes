import cv2


def mousePoints(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\joker.jpg")
cv2.imshow('Img', img)
cv2.setMouseCallback('Img', mousePoints)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break