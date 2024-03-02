import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,500),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,140,25))
cv2.putText(img,"Mars",(125,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(2,31,175))
cv2.putText(img,"Venus",(190,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"Earth",(285,175),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
cv2.putText(img,"Mercury",(365,170),cv2.FONT_HERSHEY_COMPLEX,0.5,(128,128,128))
cv2.putText(img,"Jupiter",(570,70),cv2.FONT_HERSHEY_COMPLEX,0.5,(93,100,100))
cv2.putText(img,"Saturn",(820,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(224,255,255))
cv2.putText(img,"Uranus",(970,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1115,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(250,255,214))

cv2.imshow("output",img)
cv2.waitKey(0)