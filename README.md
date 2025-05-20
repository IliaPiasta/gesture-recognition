# 🤖 Gesture Recognition

A real-time hand gesture recognition system using computer vision.

## 🛠 Technologies

- Python 3.8+
- OpenCV
- numpy
- MediaPipe
- logging
- collections
- (optional) TensorFlow / PyTorch

## ⚠️ Note about Python versions

mediapipe only works with Python 3.8 to 3.11.  
If you're using Python 3.12 or newer, it won't install — pip won't find it.

### ✅ What to do:
- Use Python 3.10 if possible (it's the most stable).
- Create a virtual environment like this:

```bash
  # Example if you have Python 3.10 installed
  path\to\python310.exe -m venv .venv
  .venv\Scripts\activate

  pip install --upgrade pip
  pip install mediapipe
```

If you’re not sure which Python version you have, run:

```bash
# cmd
python -- version
```

## 🚀 Getting Started

```bash
git clone https://github.com/IliaPiasta/gesture-recognition.git
cd gesture-recognition
pip install -r requirements.txt
python main.py
```

## ✋ Recognized Gestures

- 👍 THUMB_UP
- 👎 THUMB_DOWN
- 🤲 OPEN_PALM  
- 🫱 Movement: RIGHT  
- 🫲 Movement: LEFT

## 📂 Project Structure

```
gesture-recognition/
│
├── recognitaion/
│   ├── ExponentialSmoother.py // Applies exponential smoothing to gesture input
│   ├── GestureRecognizer.py // Contains the main gesture recognition logic
│   └── MovementDetector.py // Detects and interprets hand movement: right, left
├── main.py //  Entry point of the application
└── readme.txt // Documentation file
```

## 📌 TODO

- [ ] Add more gestures  
- [ ] Web interface (Streamlit/Flask)  
- [ ] Save custom gestures

### 📬 Contact

Questions or suggestions? Open an [Issue](https://github.com/IliaPiasta/gesture-recognition/issues) or email factsmens@gmail.com
