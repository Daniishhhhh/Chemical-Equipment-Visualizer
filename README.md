🧪 Chemical Equipment Parameter Visualizer
Hybrid Web + Desktop Data Analytics Application

A full-stack hybrid application that visualizes chemical equipment parameters from CSV files using a shared Django REST backend, a React Web frontend, and a PyQt5 Desktop application.

Built as part of the Intern Screening Task – Hybrid Web + Desktop Application.

🚀 Project Features
✅ Core Functionalities

📂 CSV Upload (Web + Desktop)

📊 Real-time Data Visualization

📈 Summary Analytics

🗂️ Upload History Management (Last 5 Records)

📄 PDF Report Generation

🔐 User Authentication

🔄 Shared Backend API

🏗️ Architecture Overview
React Web App     PyQt5 Desktop App
       │                 │
       └──── REST API ───┘
              │
         Django Backend
              │
           SQLite DB

🧰 Tech Stack
Layer	Technology
Frontend (Web)	React.js + Chart.js
Frontend (Desktop)	PyQt5 + Matplotlib
Backend API	Django + Django REST Framework
Data Processing	Pandas
Database	SQLite
Version Control	Git + GitHub
Deployment (Optional)	Render
📁 Project Structure
Chemical-Equipment-Visualizer/
│
├── backend/
│   ├── chemical_backend/
│   ├── equipment/
│   ├── manage.py
│   ├── requirements.txt
│
├── web-frontend/
│   ├── src/
│   ├── package.json
│
├── desktop-app/
│   ├── main.py
│   ├── api_client.py
│
└── README.md

⚙️ Local Setup Instructions
🔹 Backend Setup (Django)
Step 1 — Navigate to backend
cd backend

Step 2 — Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Run Migrations
python manage.py migrate

Step 5 — Create Admin User
python manage.py createsuperuser

Step 6 — Start Backend Server
python manage.py runserver


Backend will run at:

http://127.0.0.1:8000/

🔹 Web Frontend Setup (React)
Step 1 — Navigate to frontend
cd web-frontend

Step 2 — Install Packages
npm install

Step 3 — Start Web App
npm run dev


Web app runs at:

http://localhost:5173/

🔹 Desktop App Setup (PyQt5)
Step 1 — Navigate to desktop app
cd desktop-app

Step 2 — Install Dependencies
pip install -r requirements.txt

Step 3 — Launch Desktop Application
python main.py

🔐 Authentication

Login is required to access APIs

Uses Django session authentication

Same login credentials work for:

Web App

Desktop App

📊 API Endpoints
Endpoint	Method	Purpose
/api/upload-csv/	POST	Upload CSV file
/api/latest-summary/	GET	Get latest dataset summary
/api/history/	GET	Last 5 uploads history
/api/generate-pdf/	GET	Generate PDF report
/api/auth/login/	POST	User login
📄 CSV Format (Sample)

Your CSV file must contain these columns:

Equipment Name
Type
Flowrate
Pressure
Temperature


Example:

Pump-1, Pump, 20, 5, 80
Valve-2, Valve, 15, 3, 65

📦 PDF Report Feature

Automatically generated from backend

Contains:

Equipment summary

Analytics values

Available for both:

Web UI

Desktop App

🌐 Deployment (Optional)

Backend deployed on Render:

https://chemical-equipment-backend-g2bg.onrender.com


Note: Local environment is recommended for full functionality.

🎥 Demo Video

A short 2–3 minute demo video demonstrates:

Login flow

CSV upload

Charts visualization

History tracking

Desktop application integration

PDF generation

👨‍💻 Developer
Danish Sidiq                                                                                                                                                                       
Computer Science Engineering Student
