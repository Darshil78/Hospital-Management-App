from flask import Blueprint, render_template
from flask_login import current_user, login_required

from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from models.medicine import Medicine
from models.prescription import Prescription


dashboard = Blueprint(
    "dashboard",
    __name__
)


@dashboard.route("/")
@login_required
def home():
    role = (current_user.role or "Patient").capitalize()

    total_patients = Patient.query.count()
    total_doctors = Doctor.query.count()
    total_appointments = Appointment.query.count()
    total_medicines = Medicine.query.count()

    recent_appointments = Appointment.query.order_by(Appointment.created_at.desc()).limit(5).all()
    recent_medicines = Medicine.query.order_by(Medicine.created_at.desc()).limit(5).all()

    patient_prescriptions = []
    if role == 'Patient':
        matched_patient = None

        if current_user.email:
            matched_patient = Patient.query.filter_by(email=current_user.email).first()

        if not matched_patient and current_user.name:
            matched_patient = Patient.query.filter_by(name=current_user.name).first()

        if matched_patient:
            patient_prescriptions = Prescription.query.filter_by(patient_id=matched_patient.id).order_by(Prescription.date.desc()).limit(5).all()

    return render_template(
        "dashboard.html",
        role=role,
        patients=total_patients,
        doctors=total_doctors,
        appointments=total_appointments,
        medicines=total_medicines,
        appointments_list=recent_appointments,
        medicines_list=recent_medicines,
        prescriptions=patient_prescriptions,
    )