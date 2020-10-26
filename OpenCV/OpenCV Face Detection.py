import cv2

cascade_face = cv2.CascadeClassifier(r'D:\Downloads\HaarCascade classifier files\haarcascade_frontalface_alt.xml')

picture = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\lena.jpg")

gray = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY)

faces = cascade_face.detectMultiScale(gray, 1.3, 5)

for x, y, w, h in faces:
    cv2.rectangle(picture, (x, y), (x + w, y + h), (255, 255, 0), 2)
    font = cv2.FONT_ITALIC
    cv2.putText(picture, 'Face Detected', (x, y - 10), font, 0.7, (255, 255, 0), 2)

cv2.imshow('Face Detection', picture)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
