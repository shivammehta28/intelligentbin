#Two types of Cascades are made for distinguishing metal cans with non recyclable wastes like lays wraper
import numpy as np
import cv2
import sys
import serial
#Starting Serial Port for Communication with Arduino(Servo Movement)
ser=serial.Serial('COM7',9600)
#Cascades made with Tree Classifier
pepsi_cascade = cv2.CascadeClassifier('C:\Python27\pepsi_haartrain\pepsiharr.xml')
lays_cascade = cv2.CascadeClassifier('C:\Python27\lays_set\lays.xml')
video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
val=raw_input("Enter 0 or 1 to control LED:");
va=raw_input("Enter 0 or 1 to control LED:");
pepsi1=1
lays1=1
i=1
l=1
while True:
    
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if(pepsi1%10 == 0):
        print('Pepsi Founddddddd')
        i=i+1
        if(i==2):
            #Sending the instruction to arduino for servo movement 
            ser.write(val)
            exit()
    elif(lays1%10 == 0):
        print('Lays Founddddddd')
        l=l+1
        if(l==2):
            ser.write(va)
            exit()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pepsi = pepsi_cascade.detectMultiScale(gray, 1.3, 5)
    lays = lays_cascade.detectMultiScale(gray, 1.3, 5)
    if pepsi != ():
        print ('Pepsi')
        pepsi1 = pepsi1 + 1
    elif lays != ():
        print('Lays')
        lays1 = lays1 + 1
    else:
        print 'none'

        
    for (x,y,w,h) in pepsi:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        if x == 0:
            print 'Nothing'
        else:    
            cv2.putText(frame,'pepsi',(x,y+h),font,2,255)   
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
