# 🔊 Python Voice Assistant

A simple yet powerful Python-based voice assistant that listens to your voice commands, responds with text-to-speech, and performs tasks like setting timers and telling the time.

## ✨ Features

- 🎙️ Voice command recognition (using your microphone)
- 🗣️ Speech output (talks back to you)
- ⏰ Set timers using your voice
- 🕓 Get the current time
- ❌ Fallback responses for unknown commands
- 🔁 Retry mechanism if command isn't heard

## 📦 Requirements

Make sure you have Python 3.8+ installed, and then install the dependencies:

```bash
pip install -r requirements.txt 
```
If ``pyaudio`` fails to install on Windows, use this:

```bash
pip install pipwin
pipwin install pyaudio
```

## 🚀 How to Run
```bash
python Pablo.py
```

## 📝 Basic Commands You Can Say
* ``"hello"`` → Assistant will greet you

* ``"time"`` → Tells you the current time

* ``"timer"`` → Sets a timer based on your voice input

* ``"exit"`` → Exits the assistant

* ``"weather"`` → Tells current temperature

## 📁 File Structure
```
.
├── voice_assistant.py    # Main assistant script
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

## 💡 Future Ideas

* Include calendar or to-do integrations

* GUI-based assistant control panel

* Save reminders to a file

## 🧑‍💻 Author
Made with 😃 by 3boud (CS Student @ FUE)

## 📜 License
This project is for personal and educational use. Feel free to modify and expand it!

---