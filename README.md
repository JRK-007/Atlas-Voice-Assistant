# ATLAS VOICE ASSISTANT
A smart, GUI-integrated, voice-powered assistant built using Python that can interact, search, automate tasks, and respond like a human.
# 🎙️ ATLAS - Your Personal Python Voice Assistant

> A smart, GUI-integrated, voice-powered assistant built using Python that can interact, search, automate tasks, and respond like a human. Powered with NLP, APIs, and a touch of humor. 🤖💬

---

## ✨ Features

- 🗣️ **Speech Recognition** and **Text-to-Speech**
- 💻 **Tkinter GUI** with image and assistant status display
- 🌐 Open:
  - Google
  - YouTube
  - Gmail
  - StackOverflow
  - Instagram, Quora, CBSE, and custom websites
- 📸 Open **Webcam** directly from voice
- 📦 **Wikipedia integration** for info lookup
- ☁️ Real-time **weather updates** via OpenWeather API
- 📰 Fetch **latest news**
- 🧠 Ask **computational or geographical questions** (WolframAlpha)
- 🕒 Tells the time
- 🎵 Tells jokes, sings, tells riddles, and makes friendly conversation
- 🎛️ GUI includes buttons like “About” and “Close”
- 💬 Custom phrases and humor added for user engagement

---

## 🛠️ Technologies Used

| Category        | Tools & Libraries |
|----------------|-------------------|
| Voice Engine    | `pyttsx3`, `speech_recognition` |
| NLP / Knowledge | `wikipedia`, `wolframalpha` |
| Weather API     | `openweathermap.org` via `requests` |
| GUI             | `Tkinter`, `PIL` |
| Media & Audio   | `playsound`, `pyglet` |
| Browser         | `webbrowser` |
| System Control  | `os`, `subprocess`, `time` |
| Webcam Access   | `OpenCV (cv2)` |

---

## 🎬 Sample Commands

| You Say                       | ATLAS Does                                      |
|------------------------------|--------------------------------------------------|
| “Open YouTube”               | Launches YouTube in browser                      |
| “Search Python tutorial”     | Opens your search in browser                     |
| “What's the weather in Delhi”| Fetches weather details                          |
| “Tell me a joke”             | Replies with a dad joke or fun fact              |
| “Open camera”                | Launches webcam with live feed                   |
| “What's the time”            | Speaks the current time                          |
| “Who made you?”              | Gives a customized answer                        |

---

## 📷 GUI Preview

> **

---

## ⚙️ How to Run

1. Clone the repository
2. Install required libraries:
   ```bash
   pip install pyttsx3 speechrecognition wikipedia requests wolframalpha playsound pyglet opencv-python pillow
