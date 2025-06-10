# Face Mask Detection with CNN

This is a real-time face mask detection project using a Convolutional Neural Network (CNN) model trained to classify whether a person is wearing a mask or not.

## 🔍 How It Works

- Captures webcam feed using OpenCV.
- Preprocesses frames to match model input (224x224 RGB).
- Uses a pre-trained CNN (`mask_detector.h5`) for binary classification.
- Displays live results on screen with mask/no-mask labels.

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Run the App
```bash
python faceMaskDetector.py
```

Make sure your webcam is connected. For best accuracy, ensure you’re in a well-lit environment 🌞.

### 📦 Model
The model (mask_detector.h5) was taken from https://github.com/balajisrinivas

## 🧠 Tech Stack
- Python
- OpenCV
- TensorFlow / Keras
- NumPy
----
Feel free to fork, explore, or improve!