import numpy as np
import cv2

grt = cv2.imread("doctor.jpg")
grt[300:500,200:300,1]=255
grt[480:650,250:350,0]=255
cv2.imshow("dgjj",grt)
cv2.waitKey(0)
cv2.destroyAllWindows()

