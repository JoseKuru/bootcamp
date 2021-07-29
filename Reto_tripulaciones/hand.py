import cv2
import time
import mediapipe as mp
cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraws = mp.solutions.drawing_utils

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraws.draw_landmarks(img, handLms, mphands.HAND_CONNECTIONS)

    cv2.imshow('Test', img)
    cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()