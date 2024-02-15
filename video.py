import cv2
from Model import Detector

cap = cv2.VideoCapture('tree_lined_lane_-_28499 (540p).mp4')
while True:
    ret, frame = cap.read()
    # frame = cv2.resize(frame,(980,498))
    # frame = imutils.resize(frame, width=800)
    frame = Detector(frame)
    # out.write(frame)
    # cv2.resizeWindow('Car Detection System', 600, 600)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()