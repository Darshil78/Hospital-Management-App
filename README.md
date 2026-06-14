# Hospital Management System

A Flask-based hospital management application for managing patients, doctors, appointments, medicines, prescriptions, and reports.

## Features
- User registration and login
- Role-based access for Admin, Doctor, and Patient
- Patient management
- Doctor management
- Appointments
- Pharmacy and medicine inventory
- Doctor-to-patient medicine recommendations
- Report generation

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Jinja2
- Bootstrap
- ReportLab

## Project Structure
- app.py — app entry point and database initialization
- config.py — Flask configuration
- models/ — SQLAlchemy models
- routes/ — application blueprints
- templates/ — HTML templates
- static/ — CSS and JavaScript files

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install flask flask-sqlalchemy flask-login reportlab
```

## Running the App

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## Notes
- The app uses SQLite by default.
- The database is created automatically on startup.
- Admin, doctor, and patient accounts can be created through the authentication flow.

## License
This project is for educational/demo purposes.
