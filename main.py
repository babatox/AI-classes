import cv2
import numpy as np

cap = cv2.VideoCapture(0)
mode='normal'

print("""
Keyboard Controls
    e - Edge Detection (canny) 
    r - Red Filter
    g - Green Filter 
    b - Blue Filter
    n - Normal Filter
    q - Quit
""")

while True:
    ret,frame=cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if mode=='edge':
        gray = cv2.cvtColor('frame, cv2.COLOR_BGR2GRAY')
        frame = cv2.Canny(gray,100,200)
    elif mode=='red':
        frame = cv2.inRange(frame,(0, 0, 100),(80, 80, 255))
    elif mode=='green':
        frame = cv2.inRange(frame,(0, 100, 0),(80, 255, 80))
    elif mode== 'blue':
        frame = cv2.inRange(frame,(100, 0, 0),(255, 80, 80)) 

    cv2.imshow('Real-Time Filter', frame)

    key=cv2.waitKey(1) &0xFF
    if key == ord('q'):
        break
    elif key == ord('e'):
        mode= 'edge'
    elif key == ord('r'):
        mode= 'red'
    elif key == ord('g'):
        mode= 'green'
    elif key == ord('b'):
        mode= 'blue'
    elif key == ord('n'):
        mode= 'normal'

cap.release()
cv2.destroyAllWindows()
        
        
        
        