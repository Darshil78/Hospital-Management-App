from flask import Blueprint, render_template, request, redirect, url_for, flash

from extensions import db

from models.medicine import Medicine
from models.patient import Patient
from models.prescription import Prescription



pharmacy = Blueprint(
    "pharmacy",
    __name__
)




@pharmacy.route("/pharmacy")
def index():


    medicines = Medicine.query.all()


    return render_template(

        "pharmacy/index.html",

        medicines=medicines

    )





@pharmacy.route("/pharmacy/add",methods=["GET","POST"])
def add():


    if request.method=="POST":


        medicine = Medicine(


            name=request.form["name"],


            category=request.form["category"],


            company=request.form["company"],


            quantity=request.form["quantity"],


            price=request.form["price"],


            expiry_date=request.form["expiry"]

        )


        db.session.add(medicine)

        db.session.commit()



        return redirect(

            url_for("pharmacy.index")

        )



    return render_template(

        "pharmacy/add.html"

    )





@pharmacy.route("/pharmacy/recommend", methods=["GET", "POST"])
def recommend():

    patients = Patient.query.order_by(Patient.name).all()
    medicines = Medicine.query.order_by(Medicine.name).all()

    if request.method == "POST":

        patient_id = request.form.get("patient_id")
        medicine_name = request.form.get("medicine_name")
        dosage = request.form.get("dosage")
        timing = request.form.get("timing")
        instructions = request.form.get("instructions")
        diagnosis = request.form.get("diagnosis")
        date = request.form.get("date") or ""

        if patient_id and medicine_name:
            prescription = Prescription(
                patient_id=int(patient_id),
                medicine_name=medicine_name,
                dosage=dosage,
                timing=timing,
                instructions=instructions,
                diagnosis=diagnosis,
                date=date,
            )
            db.session.add(prescription)
            db.session.commit()
            flash("Medicine recommendation saved")
            return redirect(url_for("pharmacy.index"))

        flash("Please select a patient and medicine")

    return render_template(
        "pharmacy/recommend.html",
        patients=patients,
        medicines=medicines,
    )


@pharmacy.route("/pharmacy/delete/<int:id>")
def delete(id):


    medicine = Medicine.query.get_or_404(id)



    db.session.delete(medicine)

    db.session.commit()



    return redirect(

        url_for("pharmacy.index")

    )