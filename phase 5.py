import random
import time

class SensorModule:
    def __init__(self):
        self.lidar_range = 100  # meters
        self.gps_coordinates = (0.0, 0.0)

    def read_lidar(self):
        return random.randint(0, self.lidar_range)

    def read_gps(self):
        self.gps_coordinates = (
            self.gps_coordinates[0] + random.uniform(-0.01, 0.01),
            self.gps_coordinates[1] + random.uniform(-0.01, 0.01)
        )
        return self.gps_coordinates

class ActuatorModule:
    def steer(self, direction):
        print(f"Steering {direction}")

    def accelerate(self, speed):
        print(f"Accelerating at {speed} km/h")

    def brake(self):
        print("Braking!")

sensor = SensorModule()
actuator = ActuatorModule()

for _ in range(5):
    distance = sensor.read_lidar()
    gps_position = sensor.read_gps()

    print(f"Lidar Distance: {distance} meters | GPS Position: {gps_position}")

    if distance < 20:
        actuator.brake()
    else:
        actuator.accelerate(random.randint(10, 100))

    time.sleep(1)


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



