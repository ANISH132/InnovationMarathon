import cv2 
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

#Variables
width, height = 700,500
gestureThreshold = 300

#Set Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#Set HandDectector object
detector = HandDetector(detectionCon = 0.8, maxHands = 1, minTrackCon = 0.5)

while True:
    
    #Capture feed
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #Detect Hand
    hands, img = detector.findHands(img, flipType = False)
    
    if hands:
        hand1 = hands[0]                         #Only one hand recognized
      
        fingers = detector.fingersUp(hand1)      #Number of fingers UP
        # print(fingers)
        # cx, cy = hand1['center']                 #Center pt of hand
    
        #Gesture 1 - Fast Forward
        if (fingers == [1,0,0,0,1] and hand1['type'] == 'Right') or (fingers == [0,0,0,0,0] and hand1['type'] == 'Left'):
            print(fingers,' Fast Forward')
            pyautogui.press('right')
            time.sleep(1)
            
        #Gesture 2 - Rewind
        elif (fingers == [0,0,0,0,0] and hand1['type'] == 'Right') or (fingers == [1,0,0,0,1] and hand1['type'] == 'Left'):
            print(fingers," Rewind")
            pyautogui.press('left')
            time.sleep(1)
        
        #Gesture 3 - VolumeUp
        elif (fingers == [1,1,0,0,0] and hand1['type'] == 'Right') or (fingers == [1,1,0,0,0] and hand1['type'] == 'Left'):
            print(fingers," Volume Up")
            pyautogui.press('volumeup')
            time.sleep(200/1000)

        #Gesture 4 - VolumeDown
        elif (fingers == [1,1,1,0,0] and hand1['type'] == 'Right') or (fingers == [1,1,1,0,0] and hand1['type'] == 'Left'):
            print(fingers," Volume Down")
            pyautogui.press('volumedown')
            time.sleep(200/1000)

        #Gesture 5 - Pause
        elif (fingers == [0,1,1,1,1] and hand1['type'] == 'Right') or (fingers == [0,1,1,1,1] and hand1['type'] == 'Left'):
            print(fingers,' Pause')
            pyautogui.press('space')
            time.sleep(3)     

        #Gesture 6 - Play
        elif (fingers == [1,1,1,1,0] and hand1['type'] == 'Right') or (fingers == [1,1,1,1,0] and hand1['type'] == 'Left'):
            print(fingers,' Play')
            pyautogui.press('space')
            time.sleep(3)
        
        #Gesture 7 - Alt F4
        elif fingers == [1,0,1,0,0] :
            print(fingers,' Close')
            pyautogui.hotkey('Alt','f4')
            time.sleep(1)

    #Display                              
    cv2.imshow("Live Feed", img)
    
    #Break out of Loop
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


