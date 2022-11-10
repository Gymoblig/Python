import numpy as np

import cvzone.HandTrackingModule as htm
import time
import pyautogui
import cv2 
##########################
wCam, hCam = 640, 480
frameR = 150 # Redukcia Snímkov
smoothening = 2
#########################
 
pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0
 
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.HandDetector()
wScr, hScr = pyautogui.size()
print(wScr, hScr)
 
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # Záchytné body na ruke (kĺby)
        bbox1 = hand1["bbox"]  # Box okolo ruky x,y,w,h
        centerPoint1 = hand1["center"]  # Stred ruky cx,cy
        handType1 = hand1["type"]  # Určenie ruky
        x1, y1 = lmList1[8]
        x2, y2 = lmList1[12]

        fingers1 = detector.fingersUp(hand1)

                
            
        if fingers1[1] == 1 and fingers1[2] == 0  and fingers1[0] == 0 and fingers1[3] == 0 and fingers1[4] == 0:
                
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 255, 255), 2)
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening
    
            pyautogui.moveTo(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 3, (5, 0, 5), cv2.FILLED)
            plocX, plocY = clocX, clocY

                
        if fingers1[1] == 1 and fingers1[2] == 1  and fingers1[0] == 0 and fingers1[3] == 0 and fingers1[4] == 0:
            center1 = x1, y1
            center2 = x2, y2
            length, lineInfo, img = detector.findDistance(center1, center2, img) 
            print(length)
        # Kliknutie ľavým tlačidlom (Hodnota 20 = Mala by sa zmeniť v závislosti k vzialenosti kamery od ruky)
            if length < 20:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()
        
        if fingers1[2] == 0 and fingers1[1] == 0  and fingers1[0] == 1 and fingers1[3] == 0 and fingers1[4] == 1:
                break


    
    cv2.imshow("Ruky", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    cv2.waitKey(1)