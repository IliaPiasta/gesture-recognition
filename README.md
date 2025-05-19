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

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/gesture-recognition.git
cd gesture-recognition
pip install -r requirements.txt
python app.py
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

Questions or suggestions? Open an [Issue](https://github.com/iliapiasta/gesture-recognition/issues) or email factsmens@gmail.com
