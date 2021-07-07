import cv2
import numpy as np 


#piksel = cv2.imread("lambored.jpg")

#cv2.imshow("alsdjgn",piksel)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#print(piksel[(263,453)])

#print("Resmin boyutu: " +str(piksel.size))
#print("Resmin özellikleri : "+ str(piksel.shape))
#print("Resmin veri tipi: " +str(piksel.dtype))

rsm = cv2.imread("optimus.jpg")

rsm[54,62] = [255,255,255]
print(rsm)
#cv2.imshow("trans",rsm)

cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(100):
    rsm[i,i]=[255,255,255]
    
cv2.imshow("tra",rsm)

cv2.waitKey(0)
cv2.destroyAllWindows()
