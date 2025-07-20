# 🎮 Voice-Controlled Rock Paper Scissors
_A game for the Inclusive Game Design Challenge_

## 🧩 Overview
This project was built for the **Inclusive Game Design Challenge** with the goal of designing a fun, meaningful, and **accessible game for children with disabilities**, particularly those who are **visually impaired**.

The game enables children to play **Rock Paper Scissors using voice commands**, eliminating the need for any visual interaction. It speaks all prompts and results using text-to-speech, making it completely audio-driven.

---

## 👥 Who It's For
Designed specifically for:
- Children with **visual impairments** (blind or low vision)
- Children with **motor impairments** (hands-free play)
- Also suitable for children who prefer auditory interaction

---

## 💡 Accessibility Features
- 🎤 **Voice recognition** using Google Speech API (`speech_recognition`)
- 🔊 **Audio feedback** for all prompts, choices, and results (`gTTS` + `pygame`)
- 🖱️ **No need for screen, keyboard, or mouse interaction**
- 🧠 Simple logic and feedback structure for **low cognitive load**

---

## 🚀 How It Works
1. The game introduces itself and asks for the player's move.
2. The user **speaks** “rock”, “paper”, or “scissor”.
3. The computer announces its choice.
4. The winner is declared by voice.
5. The game continues for 3 rounds, then announces the final result.

---

## ⚙️ Tech Stack
- **Python 3**
- [`gTTS`](https://pypi.org/project/gTTS/) – Text-to-Speech
- [`pygame`](https://pypi.org/project/pygame/) – Audio playback
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – Voice command input

---

## 📦 Installation & Run

### ✅ Prerequisites
- Python 3.x
- Microphone & speaker enabled
- Internet connection (for Google Speech and gTTS)

### 🔧 Setup
```bash
pip install gTTS pygame SpeechRecognition
