import cv2
from gaze_tracking import GazeTracking
import pyautogui
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
speed = 20
last = " "
pyautogui.FAILSAFE = False

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    '''if gaze.is_blinking():
        text = "Blinking"
        pyautogui.typewrite ('Click ')'''
    if gaze.is_top():
        if last == "T":
            speed = speed + 10
        else:
            speed = 20
        pyautogui.moveRel(0, -speed)
        #pyautogui.typewrite ('T ')
        last = "T"
        
    elif gaze.is_bottom():
        if last == "B":
            speed = speed + 10
        else:
            speed = 20
        pyautogui.moveRel(0, speed)
        #pyautogui.typewrite ('B ')
        last = "B"
        
    elif gaze.is_left():
        if last == "L":
            speed = speed + 10
        elif last == "R":
            pyautogui.click(button='right')
            speed = 0
        else: speed = 20
        pyautogui.moveRel(-speed, 0)
        #pyautogui.typewrite ('L ')
        last = "L"
        
    elif gaze.is_right():
        if last == "R":
            speed = speed + 10
        elif last == "L":
            pyautogui.click()
            speed = 0
        else: speed = 0
        pyautogui.moveRel(speed, 0)
        #pyautogui.typewrite ('R ')
        last = "R"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
