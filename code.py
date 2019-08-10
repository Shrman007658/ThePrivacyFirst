import cv2
import pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()

f_c = cv2.CascadeClassifier('face_cascade.xml')
cap = cv2.VideoCapture(0)
count=0

def detect(img):
    faces = f_c.detectMultiScale(img, 1.3, 5)
    count = 0;
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 5)
        count = count + 1
    if count > 1:
        keyboard.press(Key.cmd)
        keyboard.press('m')
        keyboard.release('m')
        keyboard.release(Key.cmd)
    cv2.imshow('frame', img)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detect(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




