import cv2

cap = cv2.VideoCapture(r"D:\Downloads\OpenCV\video.mp4")
count = 0
while True:

    timer1 = cv2.getTickCount()
    success, img = cap.read()

    timer2 = cv2.getTickCount()
    fps = cv2.getTickFrequency() / ((timer2 - timer1) * 10)
    cv2.putText(img, f'FPS: {fps}', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    count = count + 1

    if success == True:
        cv2.imshow('Feed', img)
    else:
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(100) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

# print(count)
