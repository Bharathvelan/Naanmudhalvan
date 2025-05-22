import cv2

def get_frame():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        yield frame


import cv2
import numpy as np

def detect_line(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([20, 100, 100])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest)
        center = x + w // 2
        return center, mask

    return None, mask


import random

def get_distance():
    return random.randint(5, 100)  # distance in cm


def control_logic(line_pos, distance):
    if distance < 20:
        return "STOP - Obstacle Ahead"

    if line_pos is None:
        return "Searching for line..."

    if line_pos < 200:
        return "Turn Left"
    elif line_pos > 440:
        return "Turn Right"
    else:
        return "Move Forward"


import cv2
from vision import detect_line
from sensors import get_distance
from controller import control_logic

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    line_pos, mask = detect_line(frame)
    distance = get_distance()
    decision = control_logic(line_pos, distance)

    print(f"Distance: {distance} cm | Line: {line_pos} | Action: {decision}")
    cv2.putText(frame, decision, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Camera", frame)
    cv2.imshow("Line Detection", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
