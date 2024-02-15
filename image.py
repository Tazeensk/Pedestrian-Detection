import cv2
import imutils
from Model import Detector

img = cv2.imread('photo1.jpg')
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()