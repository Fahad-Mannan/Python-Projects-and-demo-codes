import cv2


def decode_fourcc(fourcc):
    fourcc = int(fourcc)
    fourcc_code = ''.join([chr((fourcc>>8*i) & 0xFF) for i in range(4)])
    return fourcc_code


cap = cv2.VideoCapture(r"D:\Academia\Fahad's Projects\OpenCV\video.mp4")

fourcc = cap.get(cv2.CAP_PROP_FOURCC)
fourcc = decode_fourcc(fourcc)

print(fourcc)