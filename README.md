# 🦟 Computer Vision Game: Mosquito Killer

A **real-time gesture-controlled game** powered by **Computer Vision**, built using **OpenCV**, **MediaPipe**, and **Pygame**.  
This project demonstrates how artificial intelligence and computer vision can create touchless, intuitive gaming experiences — where you play using only your hand movements.

---

## 🎮 Overview

**Mosquito Killer** is an interactive computer vision–based game that replaces traditional controllers with **hand-tracking input**.  
The system detects and tracks your hand gestures via a webcam and maps them to in-game actions in real time.

- 👋 Move your hand to control the cursor  
- ✊ Close your hand to hit mosquitoes and earn points  
- 🐝 Avoid hitting bees, or you’ll lose points  
- ⏱️ The game runs for a fixed duration and displays your final score  

Developed as part of the **Computer Graphics & Image Processing (CGIP)** course, this project highlights the integration of **AI, image processing, and gaming**.

---

## ✨ Features

- 🎯 Real-time hand tracking using MediaPipe  
- 🖐️ Gesture recognition (open/closed hand detection)  
- 🕹️ Dynamic game logic using Pygame  
- 🔊 Sound effects and background music  
- 📊 Scoring and countdown timer  
- 🎬 Start and Game Over screens  
- 💻 Fully hands-free gameplay

---

## 🧠 System Architecture

1. **Camera Input:** Captures live feed from the webcam.  
2. **Preprocessing:** Converts frames to RGB for MediaPipe analysis.  
3. **Hand Tracking:** Detects hand landmarks and identifies open/closed states.  
4. **Game Engine:** Pygame updates the game state, visuals, and score.  
5. **Display Output:** Renders background, objects, score, and timer dynamically.

---

## 🧩 Module Description

| Module | Description |
|---------|-------------|
| **settings.py** | Contains configuration constants such as screen size, FPS, and object count. |
| **mosquito.py** | Defines mosquito sprite behavior – movement and collision handling. |
| **bee.py** | Defines bee sprite behavior – acts as a penalty when hit. |
| **cursor.py** | Uses MediaPipe and OpenCV to track the player’s hand and detect gestures. |
| **game.py** | Core logic for rendering, collision detection, and score calculation. |
| **main.py** | Entry point integrating camera feed, hand tracking, and game engine. |
| **requirements.txt** | Lists all external libraries required to run the game. |

---

## 📦 Installation & Setup

### 1️ Clone the Repository

git clone https://github.com/MannanShariff/COMPUTER-VISION-GAME-MOSQUITO-KILLER.git
cd COMPUTER-VISION-GAME-MOSQUITO-KILLER

### 2 Install Dependencies

pip install -r requirements.txt

### 3 Run the Game

python main.py

---

🕹️ Gameplay Instructions

Action	Description
✋ Open Hand	Cursor moves across the screen
✊ Closed Hand	Hit nearby mosquitoes to gain points
🐝 Avoid Bees	Hitting bees reduces score
⏱️ Timer Ends	Game over — final score displayed
🔁 Restart	Press “R” key on the Game Over screen
❌ Quit	Press “Q” key to exit the game

---

🧩 How It Works (Under the Hood)

OpenCV captures frames from your webcam.
MediaPipe Hands API detects 21 hand landmarks and identifies whether the hand is open or closed.
Detected coordinates are mirrored horizontally to create a natural interaction feel.
These coordinates are passed to Pygame, which updates the hand cursor and sprite positions.
The game engine checks collisions:
✅ Mosquito hit → +1 point
❌ Bee hit → −2 points
Sound effects and graphics are rendered in real-time to enhance the gameplay experience.

---

Snapshots

<img width="1435" height="845" alt="Screenshot 2025-11-11 190935" src="https://github.com/user-attachments/assets/e7689730-2020-458c-afa3-47199f62256a" />
<img width="1366" height="798" alt="Screenshot 2025-11-11 191000" src="https://github.com/user-attachments/assets/e34f82be-867f-4826-a053-35f6472b475f" />
<img width="1272" height="775" alt="Screenshot 2025-11-11 191037" src="https://github.com/user-attachments/assets/77e9e21c-f11c-41bd-beef-f09b8aa37f2b" />
<img width="1202" height="706" alt="Screenshot 2025-11-11 222813" src="https://github.com/user-attachments/assets/ba2da148-66b8-47cc-ba58-6a0c7f9cebc3" />

---

🏁 Conclusion

The Computer Vision Game: Mosquito Killer demonstrates how computer vision and AI can enhance user interaction through gesture-based gaming.
By combining OpenCV for video processing, MediaPipe for hand tracking, and Pygame for graphics and logic, this project creates a fully hands-free, real-time entertainment experience.

It stands as a strong example of how AI and image processing can redefine human-computer interaction for gaming, learning, and beyond.

---

Developed by: Mannan Shariff

---

✅ This version includes:
- All gameplay & setup instructions  
- “How It Works” internal explanation  
- Snapshots table  
- Conclusion  
  
Would you like me to make a **badge header (Python / OpenCV / MediaPipe / License)** version for the top — to make it look like a polished open-source repo?

---
