import cv2 
from cvzone.HandTrackingModule import HandDetector
import webbrowser, pyautogui
import time

#Variables
width, height = 700,500
gestureThreshold = 300

#Set Webcam
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

#Set HandDectector object
detector = HandDetector(detectionCon = 0.8, maxHands = 2, minTrackCon = 0.5)

while True:
    
    #Capture feed
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #Detect Hand
    hands, img = detector.findHands(img, flipType = False)
    
    if len(hands)==1:
        hand1 = hands[0]                         #Only one hand recognized
      
        fingers = detector.fingersUp(hand1)      #Number of fingers UP
        # print(fingers)
        # cx, cy = hand1['center']                 #Center pt of hand
    
        #Gesture 1 -Lt Thumb or Rt Little Finger- Fast Forward
        if (fingers == [1,0,0,0,1] and hand1['type'] == 'Right') or (fingers == [0,0,0,0,0] and hand1['type'] == 'Left'):
            print(fingers,' Fast Forward')
            pyautogui.press('right')
            time.sleep(1)
            
        #Gesture 2 -Rt Thumb or Lt Little Finger- Rewind
        elif (fingers == [0,0,0,0,0] and hand1['type'] == 'Right') or (fingers == [1,0,0,0,1] and hand1['type'] == 'Left'):
            print(fingers," Rewind")
            pyautogui.press('left')
            time.sleep(1)
        
        #Gesture 3 -Index Finger- VolumeUp
        elif (fingers == [1,1,0,0,0] and hand1['type'] == 'Right') or (fingers == [1,1,0,0,0] and hand1['type'] == 'Left'):
            print(fingers," Volume Up")
            pyautogui.press('volumeup')
            time.sleep(200/1000)

        #Gesture 4 -Index, Middle Fingers- VolumeDown
        elif (fingers == [1,1,1,0,0] and hand1['type'] == 'Right') or (fingers == [1,1,1,0,0] and hand1['type'] == 'Left'):
            print(fingers," Volume Down")
            pyautogui.press('volumedown')
            time.sleep(200/1000)

        #Gesture 5 -Index, Middle, Ring and Little Fingers- Pause
        elif (fingers == [0,1,1,1,1] and hand1['type'] == 'Right') or (fingers == [0,1,1,1,1] and hand1['type'] == 'Left'):
            print(fingers,' Pause')
            pyautogui.press('space')
            time.sleep(3)     

        #Gesture 6 -Index, Middle and Ring Fingers - Play
        elif (fingers == [1,1,1,1,0] and hand1['type'] == 'Right') or (fingers == [1,1,1,1,0] and hand1['type'] == 'Left'):
            print(fingers,' Play')
            pyautogui.press('space')
            time.sleep(3)
        
        #Gesture 7 -Middle Finger- Alt F4
        elif fingers == [1,0,1,0,0] :
            print(fingers,' Close')
            pyautogui.hotkey('Alt','f4')
            time.sleep(1)
        
    if len(hands) ==2: 
        #Gesture 8 - Both Fists closed
        
        if (detector.fingersUp(hands[0])==[1,0,0,0,0]) and detector.fingersUp(hands[1])==[1,0,0,0,0]: 
                webUrl = webbrowser.open('https://www.google.com')
                time.sleep(900/1000)
                data = 'https://www.youtube.com/watch?v=xvFZjo5PgG0' 
                pyautogui.press(x for x in data)
                time.sleep(300/1000)
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.click(x=4, y=500, clicks=2)

    

    #Display                              
    cv2.imshow("Live Feed", img)
    
    #Break out of Loop
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


