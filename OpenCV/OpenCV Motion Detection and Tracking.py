import cv2

cap = cv2.VideoCapture(r"D:\Academia\Fahad's Projects\OpenCV\vtest.avi")

success, frame1 = cap.read()
success, frame2 = cap.read()

while True:
    diff = cv2.absdiff(frame1, frame2)
    blur = cv2.GaussianBlur(diff, (5, 5), 1)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, (5, 5), iterations=3)

    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, 'Moving', (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 2)

    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    cv2.putText(frame1, 'FEED: MOVEMENT', (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow('FEED', frame1)

    frame1 = frame2
    success, frame2 = cap.read()

    if success == False:
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
