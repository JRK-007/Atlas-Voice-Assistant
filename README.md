# 🎙️ ATLAS - Your Personal Python Voice Assistant

> A smart, GUI-integrated, voice-powered assistant built using Python that can interact, search, automate tasks, and respond like a human. Powered with NLP, APIs, and a touch of humor. 🤖💬

---

## ✨ Features

* 🗣️ **Speech Recognition** and **Text-to-Speech**
* 💻 **Tkinter GUI** with image and assistant status display
* 🌐 Open:

  * Google
  * YouTube
  * Gmail
  * StackOverflow
  * Instagram, Quora, CBSE, and custom websites
* 📸 Open **Webcam** directly from voice
* 📦 **Wikipedia integration** for info lookup
* ☁️ Real-time **weather updates** via OpenWeather API
* 📰 Fetch **latest news**
* 🧠 Ask **computational or geographical questions** (WolframAlpha)
* 🕒 Tells the time
* 🎵 Tells jokes, sings, tells riddles, and makes friendly conversation
* 🎛️ GUI includes buttons like “About” and “Close”
* 💬 Custom phrases and humor added for user engagement

---

## 🛠️ Technologies Used

| Category        | Tools & Libraries                |
| --------------- | -------------------------------- |
| Voice Engine    | `pyttsx3`, `speech_recognition`  |
| NLP / Knowledge | `wikipedia`, `wolframalpha`      |
| Weather API     | `requests`, `openweathermap.org` |
| GUI             | `Tkinter`, `PIL`                 |
| Media & Audio   | `playsound`, `pyglet`            |
| Browser         | `webbrowser`                     |
| System Control  | `os`, `subprocess`, `time`       |
| Webcam Access   | `OpenCV (cv2)`                   |

---

## 📷 GUI Preview

> *(Add a screenshot of `ATLAS img.jpg` here if available)*

---

## 📦 How to Install Required Libraries

Before running this project, ensure you have **Python 3.8 or higher** installed on your system.
If not, download it here ➜ [python.org/downloads](https://www.python.org/downloads/)

### ✅ Step 1: Open Your Terminal or Command Prompt

For **Windows**:

```bash
Press Win + R → type cmd → press Enter
```

For **Mac/Linux**:
Open the Terminal from Applications or press `Ctrl + Alt + T`

### ✅ Step 2: Install `pip` (if not already)

Check if `pip` is installed:

```bash
pip --version
```

If it's not installed:

```bash
python -m ensurepip --upgrade
```

### ✅ Step 3: Install All Required Libraries

Run the following command to install all dependencies:

```bash
pip install pyttsx3 speechrecognition wikipedia requests wolframalpha playsound pyglet opencv-python pillow
```

### 💡 Optional: Install via `requirements.txt`

1. Create a file named `requirements.txt`
2. Paste the following inside it:

```
pyttsx3
speechrecognition
wikipedia
requests
wolframalpha
playsound
pyglet
opencv-python
pillow
```

3. Then install all with:

```bash
pip install -r requirements.txt
```

### ✅ Step 4: Verify Installation

Launch Python in your terminal:

```bash
python
```

Then try importing these modules:

```python
import pyttsx3, speech_recognition, wikipedia, requests, wolframalpha
import playsound, pyglet, cv2, PIL
```

If no errors show up — you're all set to run **ATLAS**! 🎉

---

## 🎬 Sample Commands

| You Say                       | ATLAS Does                          |
| ----------------------------- | ----------------------------------- |
| “Open YouTube”                | Launches YouTube in browser         |
| “Search Python tutorial”      | Opens your search in browser        |
| “What's the weather in Delhi” | Fetches weather details             |
| “Tell me a joke”              | Replies with a dad joke or fun fact |
| “Open camera”                 | Launches webcam with live feed      |
| “What's the time”             | Speaks the current time             |
| “Who made you?”               | Gives a customized answer           |

---

## 🧪 Educational Applications

* Perfect for showcasing **Python GUI + Voice + API** integration
* Useful for mini-projects, hackathons, or personal automation
* Enhances understanding of **real-time AI + speech + browser control**

---

## 📁 File Structure

```bash
ATLAS.py               # Main assistant logic with GUI and voice loop
ATLAS img.jpg          # Image shown on GUI
README.md              # Project documentation
```

---

## 👤 Developed By

**Rahul Krishna J**

* LinkedIn: [linkedin.com/in/rahulkrishna-j](https://linkedin.com/in/rahulkrishna-j)
* GitHub: [JRK-007](https://github.com/JRK-007)
* Email: [rahulkrishnaofficial@gmail.com](mailto:rahulkrishnaofficial@gmail.com)

---

## 🌟 Star This Repo

If this assistant impressed you or helped inspire something cool, please give it a ⭐ and share!

---

## 🔮 Future Enhancements

* 🎵 Music playback with Spotify API
* 💬 ChatGPT integration - [on building will be updated soon]
* 🔐 Voice authentication
* 📧 Email reader/sender feature- [on building will be updated soon]
