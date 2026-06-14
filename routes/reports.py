from flask import Blueprint, render_template, make_response

from reportlab.pdfgen import canvas

import io


from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment



reports = Blueprint(
    "reports",
    __name__
)




@reports.route("/reports")
def index():


    return render_template(
        "reports/index.html"
    )





@reports.route("/reports/pdf")
def pdf():


    buffer = io.BytesIO()


    pdf = canvas.Canvas(buffer)



    pdf.setFont(
        "Helvetica",
        18
    )


    pdf.drawString(
        100,
        800,
        "Hospital Management System Report"
    )



    pdf.setFont(
        "Helvetica",
        12
    )


    pdf.drawString(

        100,

        750,

        f"Total Patients : {Patient.query.count()}"

    )


    pdf.drawString(

        100,

        720,

        f"Total Doctors : {Doctor.query.count()}"

    )


    pdf.drawString(

        100,

        690,

        f"Total Appointments : {Appointment.query.count()}"

    )



    pdf.save()



    buffer.seek(0)



    response = make_response(
        buffer.read()
    )


    response.headers["Content-Type"]="application/pdf"


    response.headers["Content-Disposition"]="attachment; filename=report.pdf"



    return response