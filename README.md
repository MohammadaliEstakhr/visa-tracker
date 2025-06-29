# 📌 Visa Tracker – Smart Visa Application Management System

![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Django](https://img.shields.io/badge/backend-Django-blue)
![Chart.js](https://img.shields.io/badge/dashboard-Chart.js-orange)
![Status](https://img.shields.io/badge/status-Production%20Ready-success)

---

## 🧠 Overview

**Visa Tracker** is a full-featured Django web application designed to manage, track, and analyze visa applications.

Built with:
- Django, SQLite, Bootstrap 5
- REST API + Swagger
- Chart.js Dashboard
- Unit Testing
- Email Notification (Gmail)

This project was developed to showcase professional, scalable, and testable architecture — ideal for showcasing Full Stack and backend engineering skillsets, especially in tech-based visa applications (e.g. Global Talent).

---

## 🚀 Features

- 🔐 User registration, login/logout system (Django-Allauth)
- 📤 Submit visa applications with attachments
- 📊 Interactive dashboard with Pie, Doughnut, and Bar charts
- 📁 Export applications to PDF / CSV
- 📧 Email confirmation after submission (Gmail App Password support)
- 🌐 REST API with Swagger UI (`/api/docs/`)
- ✅ Unit tested using Django TestCase
- 🎨 Professional UI using Bootstrap 5

---

## 📸 Screenshot

![Dashboard Screenshot](https://user-images.githubusercontent.com/your-image-url/dashboard.png)

---

## 🛠 Installation

```bash
git clone https://github.com/YourUsername/visa-tracker.git
cd visa-tracker
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
---

## 📦 Directory Structure

```text
visa_tracker/
├── core/                            # Main Django app with business logic
│   ├── templates/                   # HTML templates (e.g. dashboard, forms)
│   ├── static/                      # Static files (CSS, JS, icons)
│   ├── views.py                     # All main views (home, dashboard, submission)
│   ├── models.py                    # Data models for visa applications
│   ├── urls.py                      # App-level URL routing
│   ├── forms.py                     # Django forms for application input
│   └── tests/                       # Unit tests directory
│       └── test_views.py            # Tests for views and form submission
├── visa_tracker/                    # Project-level settings
│   ├── settings.py                  # Django settings file
│   ├── urls.py                      # Main URL configuration
│   └── wsgi.py                      # WSGI entry point for deployment
├── media/                           # Uploaded files (CVs, docs)
├── staticfiles/                     # Collected static files for deployment
├── db.sqlite3                       # SQLite database (development only)
├── manage.py                        # Django management script
├── requirements.txt                 # Project dependencies
└── README.md                        # Project overview and documentation
