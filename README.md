# Project : Abnormal Traffic Detection System

## Introduction

Abnormal Traffic Detection is an ML-based system that identifies unusual patterns in traffic flow, vehicle behavior, or network activity. It detects anomalies like traffic spikes, wrong-way movement, or suspicious logs using trained models. Ideal for smart cities and traffic control rooms, it automates monitoring and ensures quick response to potential threats or accidents.

## Features

•	Upload traffic data (CSV, logs, or frames)
•	Automatic anomaly detection based on trained ML model
•	Real-time flagging of abnormal patterns
•	Simple, user-friendly interface using Streamlit
•	Supports basic preprocessing, visualization, and analysis
•	Highlights potential issues for review
•	Can be extended to live video feeds or sensor data

## Tech Stack

•	Python
•	Scikit-learn (for machine learning)
•	Pandas & NumPy (for data handling)
•	Matplotlib / Seaborn (for visualization)
•	OpenCV (optional, if video/image is involved)

## Installation

### Database Setup

•	Option 1: Using MySQL
1.	1. Open XAMPP and start MySQL and Apache.
2.	2. Go to phpMyAdmin: http://localhost/phpmyadmin
3.	3. Create a new database named: abnormal_traffic
4.	4. Import the SQL file: Database/abnormal_traffic_detection.sql
•	Option 2: Using SQLite (Default)
•	No setup needed — Django will use SQLite if not configured otherwise.

### Run Migrations & Create Admin User

•	Run the following commands in your terminal:
•	python manage.py makemigrations
•	python manage.py migrate
•	python manage.py createsuperuser  # Optional (create admin account)

### Run the Web Server

•	Start the Django development server:
•	python manage.py runserver
•	Then open your browser and go to: http://127.0.0.1:8000
•	You should now see the application homepage.

## Project Video

https://drive.google.com/file/d/18AdCNMzvAv-UJ57lcL_rDMLi8_DwRGje/view?usp=drivesdk

## Connect with me

- [LinkedIn](https://www.linkedin.com/in/nasreenshaik21/)
- [GitHub](https://www.github.com/ShaikScripts/)
