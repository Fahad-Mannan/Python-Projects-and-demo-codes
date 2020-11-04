import cv2


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(img, 'Tracking', (40, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


cap = cv2.VideoCapture(r"D:\Academia\Fahad's Projects\OpenCV\vtest.avi")

# tracker = cv2.TrackerMOSSE_create()         # This is fast but less accurate
tracker = cv2.TrackerCSRT_create()  # This is slow but more accurate
success, img = cap.read()

bbox = cv2.selectROI('tracking', img, False)
tracker.init(img, bbox)

while True:
    timer = cv2.getTickCount()

    success1, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, 'Lost', (40, 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, 'FPS: ' + str(int(fps)), (40, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (55, 255, 255), 2)
    cv2.imshow("tracking", img)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    if success1 == False:
        cv2.destroyAllWindows()
        break