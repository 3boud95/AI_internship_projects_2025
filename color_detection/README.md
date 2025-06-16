# 🎨 Color Identifier in Image or Video with OpenCV

This is a Python-based tool to identify and display the name of a color when you click anywhere on an image or a video. It works using OpenCV and a color database in CSV format.
## 🚀 Features
- Supports both images and videos

- Detects color names using RGB matching

- Displays a color label bar and RGB values when you click

- Closes easily by pressing Esc

## 🖥 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the app:
   ```bash
   python color_detector.py
   ```
You’ll be prompted to enter a file path:

For images: JPG, PNG, etc.

For videos: MP4, AVI, etc.

Click anywhere inside the window to see the color name and RGB values.

## 🧠 Technologies Used
- Python
- OpenCV
- Pandas

## 📂 Dataset
``color.csv`` contains RGB values and color names sourced from a public dataset.

## 💡 Notes
- Press Esc to exit at any time.

- Video detection updates in real time frame-by-frame.

- RGB color matching is done via Manhattan distance.



---
Made with 💪 for an AI Internship project.