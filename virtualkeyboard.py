import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone import *
import cvzone
from mediapipe import *
from time import sleep
import numpy as np
from pynput.keyboard import Controller

#for open the camera
cap=cv2.VideoCapture(0)

#size of background
cap.set(3,1280)
cap.set(4,720)

#use to detect hand
detector=HandDetector(detectionCon=0.8)

#keys show on screen
keys=[["Q","W","E","R","T","Y","U","I","O","P"],
      ["A","S","D","F","G","H","J","K","L",";"],
      ["Z","X","C","V","B","N","M",",",".","/"]]

finalText=""

keyboard=Controller()

def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        cvzone.cornerRect(img,(button.pos[0],button.pos[1],button.size[0],button.size[1]),20,rt=0)
        cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,255),cv2.FILLED)
        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,67,234),4)

    return img    



