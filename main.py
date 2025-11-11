import cv2
from cursor import HandTracker
from game import Game

assets = {
    'bg': 'assets/bg.jpg',
    'hand': 'assets/hand.png',
    'bee': 'assets/bee.png',
    'hit': 'assets/hit.wav',
    'damage': 'assets/damage.wav',
    'bg_music': 'assets/music.wav',
    'mosquito1': 'assets/mosquito-1.png',
    'mosquito2': 'assets/mosquito-2.png',
    'mosquito3': 'assets/mosquito-3.png',
    'mosquito4': 'assets/mosquito-4.png',
    'mosquito5': 'assets/mosquito-5.png'
}

tracker = HandTracker()
game = Game(assets)

cap = cv2.VideoCapture(0)

# Show start screen first
game.start_screen()

while True:
    while game.running:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hand_pos, hand_closed = tracker.process(frame)
        game.update(hand_pos, hand_closed)

        # Show camera feed
        if hand_pos:
            color = (0, 255, 0) if not hand_closed else (0, 0, 255)
            cv2.circle(frame, hand_pos, 10, color, -1)

        cv2.imshow("Your Camera Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            game.running = False
            break

    # When game ends, show game over screen
    if game.game_over:
        action = game.game_over_screen()
        if action == 'restart':
            game.start_screen()
            continue
        else:
            break

cap.release()
cv2.destroyAllWindows()
