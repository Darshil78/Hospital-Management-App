import sys
from pathlib import Path

from flask import Flask

ROOT_DIR = Path(__file__).resolve().parent


def ensure_venv_on_path():
    candidates = [
        ROOT_DIR / ".venv" / "Lib" / "site-packages",
        ROOT_DIR / ".venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages",
        ROOT_DIR / "venv" / "Lib" / "site-packages",
        ROOT_DIR / "venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages",
    ]

    for path in candidates:
        if path.exists() and str(path) not in sys.path:
            sys.path.insert(0, str(path))


ensure_venv_on_path()

from config import Config
from extensions import db, login_manager



def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Models import
    from models.user import User
    from models.patient import Patient
    from models.doctor import Doctor
    from models.appointment import Appointment
    from models.prescription import Prescription
    from models.medicine import Medicine

    # Routes import
    from routes.auth import auth
    from routes.dashboard import dashboard
    from routes.patients import patients
    from routes.doctors import doctors
    from routes.appointments import appointments
    from routes.pharmacy import pharmacy
    from routes.reports import reports

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(patients)
    app.register_blueprint(doctors)
    app.register_blueprint(appointments)
    app.register_blueprint(pharmacy)
    app.register_blueprint(reports)

    with app.app_context():
        db.create_all()
        try:
            from sqlalchemy import text
            conn = db.engine.connect()

            appointment_columns = conn.execute(text("PRAGMA table_info(appointment)")).fetchall()
            appointment_names = {col[1] for col in appointment_columns}
            if 'visited_before' not in appointment_names:
                conn.execute(text("ALTER TABLE appointment ADD COLUMN visited_before BOOLEAN DEFAULT 0"))
            if 'old_report' not in appointment_names:
                conn.execute(text("ALTER TABLE appointment ADD COLUMN old_report TEXT"))

            prescription_columns = conn.execute(text("PRAGMA table_info(prescription)")).fetchall()
            prescription_names = {col[1] for col in prescription_columns}
            if 'medicine_name' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN medicine_name VARCHAR(200)"))
            if 'dosage' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN dosage VARCHAR(100)"))
            if 'timing' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN timing VARCHAR(100)"))
            if 'meal_instruction' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN meal_instruction VARCHAR(100)"))
            if 'instructions' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN instructions TEXT"))
            if 'diagnosis' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN diagnosis TEXT"))
            if 'date' not in prescription_names:
                conn.execute(text("ALTER TABLE prescription ADD COLUMN date VARCHAR(50)"))

            conn.commit()
        except Exception:
            pass

    return app


@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

app = create_app()

if __name__ == "__main__":

    app.run(debug=True)

    