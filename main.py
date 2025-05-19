import cv2
import time
import numpy as np
import pyautogui
import mediapipe as mp
import logging
import sys
from collections import deque

from recognitaion.ExponentialSmoother import ExponentialSmoother
from recognitaion.GestureRecognizer import GestureRecognizer
from recognitaion.MovementDetector import MovementDetector

logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO, datefmt='%H:%M:%S')

# --- UI Drawing ---
def draw_grid(frame, rows=6, cols=8, color=(200, 200, 200), thickness=1):
    h, w = frame.shape[:2]
    for i in range(1, cols):
        cv2.line(frame, (w*i//cols, 0), (w*i//cols, h), color, thickness)
    for j in range(1, rows):
        cv2.line(frame, (0, h*j//rows), (w, h*j//rows), color, thickness)

def draw_gesture(frame, gesture_name, color, y=110):
    cv2.putText(frame, gesture_name, (20, y), cv2.FONT_HERSHEY_SIMPLEX, 1.4, color, 2)

# --- Main Application ---
class GestureApp:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            logging.error("Cannot open camera")
            sys.exit(1)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

        self.smoother = ExponentialSmoother(alpha=0.25)
        self.gesture_recognizer = GestureRecognizer()
        self.movement_detector = MovementDetector()
        self.gesture_history = deque(maxlen=12)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            draw_grid(frame)

            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(img_rgb)
            current_time = time.time()

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                xs = [hand_landmarks.landmark[i].x for i in [0, 5, 9, 13, 17]]
                center_x = int(np.mean(xs) * frame.shape[1])
                smooth_center = int(self.smoother.update(center_x))

                action = self.movement_detector.update(smooth_center, current_time)
                if action == 'RIGHT':
                    draw_gesture(frame, "RIGHT", (0,255,0), y=70)
                    logging.info("Movement: RIGHT ")
                elif action == 'LEFT':
                    draw_gesture(frame, "LEFT", (255,0,0), y=70)
                    logging.info("Movement: LEFT ")

                gestures = self.gesture_recognizer.recognize(hand_landmarks)
                self.gesture_history.append(gestures)

                # Majority voting for gesture stability
                if len(self.gesture_history) == self.gesture_history.maxlen:
                    counts = {k: sum(g[k] for g in self.gesture_history) for k in gestures}
                    for gesture, count in counts.items():
                        if count > 0.8 * self.gesture_history.maxlen:
                            color = {
                                "OK": (0,255,255),
                                "THUMB_UP": (0,255,0),
                                "THUMB_DOWN": (0,0,255),
                                "OPEN_PALM": (255,255,0)
                            }[gesture]
                            draw_gesture(frame, gesture.replace("_", " "), color)
                            logging.info(f"Gesture: {gesture}")
                            break

            cv2.imshow("Gesture Recognition", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    GestureApp().run()
