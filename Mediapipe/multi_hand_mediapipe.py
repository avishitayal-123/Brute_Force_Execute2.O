import cv2 
import mediapipe as mp
import time 

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("C:/Users/Lenovo/Downloads/haarcascade_fullbody.xml")
mphands = mp.solutions.hands
hands = mphands.Hands(max_num_hands=4)
draw = mp.solutions.drawing_utils 
ctime,ptime = 0,0
while True:
    success,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rgbimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    faces = cascade.detectMultiScale(gray, 1.1, 4)
    result = hands.process(rgbimg)
    if result.multi_hand_landmarks:
        for landmark in result.multi_hand_landmarks:
            draw.draw_landmarks(img,landmark,mphands.HAND_CONNECTIONS)
    for x,y,w,h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (26, 242, 54), 2)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,f'{int(fps)} FPS',(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,255,51),3)
    cv2.imshow('Window',img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break