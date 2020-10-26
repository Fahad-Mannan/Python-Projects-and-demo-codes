import cv2

img = cv2.imread(r"D:\Academia\Fahad's Projects\OpenCV\jitu_resized.jpg")
print(img.shape)

imgCropped = img[170:360, 250:430]  # here we are just grabbing the pixels by Row and Column wise
print(imgCropped.shape)


cv2.imshow('Image', img)
cv2.imshow('Cropped Image', imgCropped)


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break