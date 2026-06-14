from flask import Blueprint, render_template, request, redirect, url_for

from extensions import db

from models.appointment import Appointment
from models.patient import Patient
from models.doctor import Doctor


appointments = Blueprint(
    "appointments",
    __name__
)



@appointments.route("/appointments")
def index():

    data = Appointment.query.all()

    return render_template(
        "appointments/index.html",
        appointments=data
    )



@appointments.route("/appointments/add", methods=["GET","POST"])
def add():


    patients = Patient.query.all()

    doctors = Doctor.query.all()



    if request.method == "POST":


        appointment = Appointment(

            patient_id=request.form["patient"],

            doctor_id=request.form["doctor"],

            appointment_date=request.form["date"],

            appointment_time=request.form["time"],

            reason=request.form.get("problem", request.form.get("reason", "")),

            visited_before=request.form.get("visited_before") == "on",

            old_report=request.form.get("old_report", "")

        )


        db.session.add(appointment)

        db.session.commit()



        return redirect(
            url_for("appointments.index")
        )


    return render_template(

        "appointments/add.html",

        patients=patients,

        doctors=doctors

    )




@appointments.route("/appointments/status/<int:id>/<status>")
def status(id,status):


    appointment = Appointment.query.get_or_404(id)


    appointment.status = status


    db.session.commit()



    return redirect(
        url_for("appointments.index")
    )




@appointments.route("/appointments/delete/<int:id>")
def delete(id):


    appointment = Appointment.query.get_or_404(id)


    db.session.delete(appointment)

    db.session.commit()



    return redirect(
        url_for("appointments.index")
    )