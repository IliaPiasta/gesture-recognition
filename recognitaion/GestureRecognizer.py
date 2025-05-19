import numpy as np
# --- Gesture Detection ---
class GestureRecognizer:
    def __init__(self):
        pass

    @staticmethod
    def dist(p1, p2):
        return np.linalg.norm(np.array([p1.x, p1.y]) - np.array([p2.x, p2.y]))

    @staticmethod
    def angle(a, b, c):
        ba = np.array([a.x - b.x, a.y - b.y])
        bc = np.array([c.x - b.x, c.y - b.y])
        cos_angle = np.clip(np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-8), -1.0, 1.0)
        return np.degrees(np.arccos(cos_angle))

    def is_finger_folded(self, landmarks, tip, pip):
        return landmarks.landmark[tip].y > landmarks.landmark[pip].y + 0.02

    def detect_ok(self, landmarks):
        thumb_tip = landmarks.landmark[4]
        index_tip = landmarks.landmark[8]
        dist_thumb_index = self.dist(thumb_tip, index_tip)
        folded = all(self.is_finger_folded(landmarks, tip, pip) for tip, pip in [(12,10), (16,14), (20,18)])
        return dist_thumb_index < 0.07 and folded

    def detect_thumb_up(self, landmarks):
        thumb_tip = landmarks.landmark[4]
        wrist = landmarks.landmark[0]
        cond1 = thumb_tip.y < wrist.y - 0.1
        cond2 = all(self.is_finger_folded(landmarks, tip, pip) for tip, pip in [(8,6), (12,10), (16,14), (20,18)])
        return cond1 and cond2

    def detect_thumb_down(self, landmarks):
        thumb_tip = landmarks.landmark[4]
        wrist = landmarks.landmark[0]
        cond1 = thumb_tip.y > wrist.y + 0.1
        cond2 = all(self.is_finger_folded(landmarks, tip, pip) for tip, pip in [(8,6), (12,10), (16,14), (20,18)])
        return cond1 and cond2

    def detect_open_palm(self, landmarks):
        fingers = [(8,6), (12,10), (16,14), (20,18), (4,2)]
        conds = [landmarks.landmark[tip].y < landmarks.landmark[pip].y - 0.02 for tip, pip in fingers]
        dist_2_5 = self.dist(landmarks.landmark[8], landmarks.landmark[20])
        return all(conds) and dist_2_5 > 0.1

    def recognize(self, landmarks):
        return {
            "OK": self.detect_ok(landmarks),
            "THUMB_UP": self.detect_thumb_up(landmarks),
            "THUMB_DOWN": self.detect_thumb_down(landmarks),
            "OPEN_PALM": self.detect_open_palm(landmarks)
        }