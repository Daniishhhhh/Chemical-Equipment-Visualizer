

********Chemical Equipment Parameter Visualizer********
(****Hybrid Web + Desktop Application****)

**📌 Project Overview**

The Chemical Equipment Parameter Visualizer is a hybrid application that runs both as a Web Application and a Desktop Application.
It allows users to upload CSV files containing chemical equipment data and visualizes important performance metrics such as flowrate, pressure, and temperature.

The system uses a single Django backend API that is consumed by both:

React Web Frontend

PyQt5 Desktop Application

This project demonstrates full-stack development, API integration, data analytics, and visualization.

**🧰 Tech Stack**
Backend
Django
Django REST Framework
Pandas
SQLite
Web Frontend
React.js
Chart.js
Axios
Desktop Application
PyQt5
Matplotlib
Requests
Version Control
Git
GitHub

**📁 Project Structure**
Chemical-Equipment-Visualizer/
│
├── backend/          → Django REST API
├── web-frontend/     → React Web Application
├── desktop-app/      → PyQt5 Desktop Application
└── README.md

**✅ Features Implemented**

CSV Upload (Web + Desktop)
Automatic Data Processing using Pandas
Summary Statistics Generation
Equipment Type Distribution Visualization
Interactive Charts (Web: Chart.js)
Desktop Charts (Matplotlib)
Upload History Management (Last 5 Records)
PDF Report Generation
Basic Authentication System
Hybrid Architecture with Common Backend API

🗂 Sample CSV Format
CSV File should contain following columns:
Equipment Name
Type
Flowrate
Pressure
Temperature

Example file: sample_equipment_data.csv

**⚙️ Backend Setup (Django)**
Step 1 — Navigate to Backend Folder
cd backend

Step 2 — Create Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Run Database Migrations
python manage.py migrate

Step 5 — Start Backend Server
python manage.py runserver


Backend will run at:
**http://127.0.0.1:8000/**

🌐 Web Frontend Setup (React)
Step 1 — Navigate to Web Folder
cd web-frontend

Step 2 — Install Packages
npm install

Step 3 — Start Development Server
npm run dev


Web App will run at:
http://localhost:5173

🖥 Desktop Application Setup (PyQt5)
Step 1 — Navigate to Desktop Folder
cd desktop-app

Step 2 — Install Dependencies
pip install -r requirements.txt

Step 3 — Run Desktop App
python main.py

**🔄 Application Workflow**

User uploads CSV file (Web or Desktop)
Backend parses file using Pandas
Summary statistics generated
Data stored in SQLite database
Charts and tables updated dynamically
History of last 5 uploads maintained
PDF report generated on request

**🔐 Authentication**

Basic login system implemented
Required for protected API endpoints
Same backend authentication shared between Web and Desktop clients

**🎥 Demo Video**

A demo video is included with the submission showing:

Backend running
Web app CSV upload and visualization
Desktop app functionality
History tracking
PDF generation

**👨‍💻 Developer**
Danish Sidiq                                                                                                                                                                                               
Computer Science & Engineering

