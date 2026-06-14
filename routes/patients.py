from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from extensions import db

from models.patient import Patient
from models.prescription import Prescription


patients = Blueprint(
    "patients",
    __name__
)



@patients.route("/patients")
def index():

    data = Patient.query.all()

    return render_template(
        "patients/index.html",
        patients=data
    )





@patients.route("/patients/add",methods=["GET","POST"])
def add():

    if request.method=="POST":

        patient = Patient(

            name=request.form["name"],

            age=request.form["age"],

            gender=request.form["gender"],

            blood_group=request.form["blood"],

            phone=request.form["phone"],

            email=request.form["email"],

            disease=request.form["disease"]

        )


        db.session.add(patient)

        db.session.commit()


        return redirect(
            url_for("patients.index")
        )


    return render_template(
        "patients/add.html"
    )





@patients.route("/patients/delete/<int:id>")
def delete(id):

    patient = Patient.query.get_or_404(id)


    db.session.delete(patient)

    db.session.commit()


    return redirect(
        url_for("patients.index")
    )


@patients.route("/recommend-medicine/<int:patient_id>", methods=["GET", "POST"])
@login_required
def recommend_medicine(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    if request.method == "POST":
        medicine_name = request.form.get("medicine_name", "").strip()
        dosage = request.form.get("dosage", "").strip()
        duration = request.form.get("duration", "").strip()
        instructions = request.form.get("instructions", "").strip()

        if not medicine_name:
            flash("Medicine name is required")
            return redirect(url_for("patients.recommend_medicine", patient_id=patient.id))

        prescription = Prescription(
            patient_id=patient.id,
            doctor_id=getattr(current_user, "id", None),
            medicine_name=medicine_name,
            dosage=dosage,
            timing=duration,
            instructions=instructions,
            diagnosis="",
            date=request.form.get("date") or "",
        )
        db.session.add(prescription)
        db.session.commit()
        flash("Medicine recommendation saved")
        return redirect(url_for("patients.index"))

    return render_template(
        "patients/recommend_medicine.html",
        patient=patient,
    )