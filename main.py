import cv2
import HandTrackingModule as htm
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

smoothen=10
plocX,plocY = 0,0
clocX,clocY = 0,0
p=0
detector = htm.handDetector(maxHands=1)
#wScr,hScr = autopy.screen.size()
while True :
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist,bbox = detector.findPosition(img)


    if len(lmlist)!=0:

        fingers = detector.fingersUp()
        print(fingers)

        if fingers[0]==1 :

            cv2.putText(img, 'Thumb', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), thickness=2, lineType=None, bottomLeftOrigin=None)
        if fingers[1]==1 :

            cv2.putText(img, 'Index', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), thickness=2, lineType=None, bottomLeftOrigin=None)
        if fingers[2] == 1:

            cv2.putText(img, 'Middle', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2,lineType=None, bottomLeftOrigin=None)
        if fingers[3] == 1:

            cv2.putText(img, 'Ring', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), thickness=2,lineType=None, bottomLeftOrigin=None)
        if fingers[4]==1 :

            cv2.putText(img, 'Pinky', (10,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), thickness=2, lineType=None, bottomLeftOrigin=None)
        if (fingers[0]==1 &fingers[4]==1):
                p=1
        if(p==1 & fingers[1]==1):
            break

    cv2.imshow("Image",img)
    cv2.waitKey(1)