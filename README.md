# 🚍 Real-time Public Transit Ghost Bus Detector

![Demo Preview](https://github.com/sumityadav2426/Real-time-Public-Transit-Ghost-Bus-Detector/blob/main/output_nagpur_realistic.gif)

> 🛰️ Real-time detection and visualization of **ghost buses** using simulated transit data over **Nagpur city map**.  
> Visualizes active (🟢 green) vs ghost (🔴 red) buses with an HD static simulation powered by Python + OpenCV.

---

## 🧠 Features

- 🗺️ Nagpur map-based static visualization  
- 🔴🟢 10,000+ red/green bus points (realistic clustering)  
- ✨ Smooth fade & pulse animation (non-movable dots)  
- ⚙️ Real-time backend simulation ready  
- 🧩 Modular backend + React frontend  
- 📩 Optional Slack/email alerts for ghost bus events  

---

## ⚙️ Setup & Run (Windows)

### 1️⃣ Backend Setup
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python generate_nagpur_static_hd.py

2️⃣ Frontend (Optional)
cd frontend
npm install
npm start

🌐 Launches dashboard at:
👉 http://localhost:3090

Project Structure
📦 Real-time-Public-Transit-Ghost-Bus-Detector
 ┣ 📁 backend
 ┣ 📁 frontend
 ┣ 📁 output_frames_nagpur
 ┣ 📜 generate_nagpur_static_hd.py
 ┣ 📜 README.md
 ┗ 📹 output_nagpur_realistic.mp4
🎬 Example Demo
🧭 Nagpur HD Output (Static Bus Visualization)
Realistic visualization of ghost and active buses over the Nagpur city map

🧩 Tech Stack
Layer	Technologies
Backend	🐍 Python (OpenCV, NumPy)
Frontend	⚛️ React.js
Maps	🌍 Leaflet / Mapbox
Real-time	🗄️ Redis / WebSocket
Alerts	📧 Slack / Email
🤝 Contributing

Pull requests and improvements are welcome!
git clone https://github.com/sumityadav2426/Real-time-Public-Transit-Ghost-Bus-Detector.git
If you want to enhance visuals, integrate real APIs, or add prediction logic — feel free to fork and experiment!

👨‍💻 Author
Sumit Yadav
📍 Nagpur, India
🔗 GitHub: sumityadav2426
