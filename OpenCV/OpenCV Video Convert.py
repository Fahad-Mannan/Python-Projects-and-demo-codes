import cv2

cap = cv2.VideoCapture(r"D:\Academia\Fahad's Projects\OpenCV\video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(r"D:\Academia\Fahad's Projects\OpenCV\prac3.mp4", fourcc, 30, (405, 720))

while True:
    success, img = cap.read()
    if success == True:
        imgResized = cv2.resize(img, (405, 720))
        out.write(imgResized)
        cv2.imshow("Actual Video", img)
        cv2.imshow("Converted Video", imgResized)
    else:
        cv2.destroyAllWindows()
        break
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
out.release()

