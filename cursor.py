import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, detection_conf=0.7, tracking_conf=0.7):
        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=detection_conf,
            min_tracking_confidence=tracking_conf
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.landmark = None
        self.closed = False

    def process(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        self.landmark = None
        self.closed = False

        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            h, w, _ = frame.shape

            # Get finger coordinates (mirrored correctly)
            x9 = int(handLms.landmark[9].x * w)
            y9 = int(handLms.landmark[9].y * h)
            x12 = int(handLms.landmark[12].x * w)
            y12 = int(handLms.landmark[12].y * h)

            # Flip horizontally so right-hand movement feels natural
            x9 = w - x9
            x12 = w - x12

            self.landmark = (w - x9, y9)


            # Detect if hand is closed (fingers down)
            if y12 > y9:
                self.closed = True

        return self.landmark, self.closed
