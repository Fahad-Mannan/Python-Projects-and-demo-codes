import cv2

path = r"D:\Academia\Fahad's Projects\OpenCV\video.mp4"
cap = cv2.VideoCapture(path)
cascadeFace = cv2.CascadeClassifier(
    r"D:\Academia\Fahad's Projects\OpenCV\HaarCascade classifier files\haarcascade_frontalface_alt.xml")
# cascadeEyes = cv2.CascadeClassifier(r"D:\Academia\Fahad's Projects\OpenCV\HaarCascade classifier files\haarcascade_eye.xml")

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascadeFace.detectMultiScale(imgGray, 1.3, 5)
    eyes = cascadeEyes.detectMultiScale(imgGray, 1.3, 5)

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (155, 155, 0), 4)
        cv2.putText(img, 'Face Detected', (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (155, 155, 0), 2)
    #    for x,y,w,h in eyes:
    #        cv2.rectangle(img, (x,y), (x+w, y+h), (155,155,0), 4)

    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break