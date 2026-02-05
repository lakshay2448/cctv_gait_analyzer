🦺 CCTV-Based Helmet, Vest & Gloves Detection System

📌 Project Overview

This project is a computer vision–based safety monitoring system that detects whether a person is wearing helmet, safety vest, and gloves using CCTV or live camera footage. The system is built using YOLOv8 for real-time object detection and is suitable for industrial safety compliance monitoring.

The model processes video streams and highlights safety violations by detecting missing protective equipment.

🚀 Key Features

Real-time detection using CCTV / webcam

Detects:

Helmet

Safety Vest

Gloves

High-speed and accurate object detection

Supports video files and live camera feed

Scalable for industrial environments

🛠️ Tech Stack

Python

YOLOv8 (Ultralytics)

OpenCV

Flask (for web interface, if used)

Roboflow (for dataset management & annotation)

📂 Project Structure
├── app.py
├── train.py
├── best.pt
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── results/
├── dataset/
├── README.md

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/helmet-vest-gloves-detection.git
cd helmet-vest-gloves-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py

📊 Model Training

Dataset prepared and annotated using Roboflow

Model trained using YOLOv8

Custom classes:

Helmet

Vest

Gloves

📸 Results

Accurate detection under different lighting conditions

Real-time bounding boxes with class labels

Works efficiently on CCTV footage


🎯 Use Cases

Industrial safety monitoring

Construction site compliance

Factory worker safety

Smart surveillance systems

🔮 Future Improvements

Alert system for safety violations

Face recognition for worker identification

Cloud-based monitoring dashboard

Mobile app integration

👨‍💻 Author

Lakshay
B.Tech CSE
University Institute of Engineering and Technology, Panjab University
