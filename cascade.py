import numpy as np
import cv2
import sys

import serial
ser=serial.Serial('COM7',9600)
pepsi_cascade = cv2.CascadeClassifier('C:\Python27\lays_haartrain\pepsiharr.xml')

video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
val=raw_input("Enter 0 or 1 to control LED:");
va=raw_input("Enter 0 or 1 to control LED:");
i=1
l=1
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    if(i%20 == 0):
        #ser.write(val)
        print('yo')
        l=l+1
        if(l==5):
            ser.write(val)
            exit()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #lays = lays_cascade.detectMultiScale(roi_gray)
    pepsi = pepsi_cascade.detectMultiScale(gray, 1.3, 5)
    #lays = lays_cascade.detectMultiScale(gray, 1.3, 5)
    
    if pepsi == ():
        print('go')
    else:
        i=i+1

        
       
    #if lays == ():
        #print 'none'
    #else:
        #print('Lays Found')
        
    for (x,y,w,h) in pepsi:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
##    for (x,y,w,h) in lays:
##        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
##        roi_gray = gray[y:y+h, x:x+w]
##        roi_color = frame[y:y+h, x:x+w]
        if x == 0:
            print 'Nothing'
        else:    
            cv2.putText(frame,'pepsi',(x,y+h),font,2,255)   
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
