import cv2
face_Casacade=cv2.CascadeClassifier(cv2.data.haarcascades +
'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture()
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()
    while True:
        ret,frame=cap.read()
        if not ret:
            print("ERROR! failedto capture image")
            break
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=face_cascade.detectMultiScale(gray,ScaleFactor=1.1,minNeighbors=5,minSize=(30,30))

        for (x, y, w, h)in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("Face-Detction, press 'q'to Quit",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows

