import numpy as np
import cv2


resim1 = cv2.imread("joker.jpg",0)
resim2 = cv2.imread("guns.jpg")
#cv2.imshow("cvar",resim1)

#print(resim)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

print(resim1.size)
print(resim2.size)
print(resim1.shape)