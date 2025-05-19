from collections import deque
import pyautogui
import numpy as np
# --- Movement Detector ---
class MovementDetector:
    def __init__(self, queue_len=5, deviation_threshold=20, delay=2.0):
        self.queue = deque(maxlen=queue_len)
        self.prev_center = None
        self.last_action_time = 0
        self.deviation_threshold = deviation_threshold
        self.delay = delay

    def update(self, center, current_time):
        action = None
        if self.prev_center is not None:
            self.queue.append(center - self.prev_center)
        self.prev_center = center

        if len(self.queue) == self.queue.maxlen and (current_time - self.last_action_time) > self.delay:
            avg_delta = np.mean(self.queue)
            if avg_delta > self.deviation_threshold:
                # pyautogui.press('up') e.g
                action = 'RIGHT'
                self.last_action_time = current_time
                self.queue.clear()
            elif avg_delta < -self.deviation_threshold:
                # pyautogui.press('down') e.g 
                action = 'LEFT'
                self.last_action_time = current_time
                self.queue.clear()
        return action