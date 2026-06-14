from flask import Blueprint,render_template,request,redirect,url_for

from extensions import db

from models.doctor import Doctor



doctors = Blueprint(
    "doctors",
    __name__
)



@doctors.route("/doctors")
def index():

    doctors = Doctor.query.all()

    return render_template(
        "doctors/index.html",
        doctors=doctors
    )





@doctors.route("/doctors/add",methods=["GET","POST"])
def add():


    if request.method=="POST":


        doctor=Doctor(

            name=request.form["name"],

            specialization=request.form["specialization"],

            qualification=request.form["qualification"],

            experience=request.form["experience"],

            phone=request.form["phone"],

            email=request.form["email"],

            available_time=request.form.get("available_time", "")

        )


        db.session.add(doctor)

        db.session.commit()


        return redirect(
            url_for("doctors.index")
        )


    return render_template(
        "doctors/add.html"
    )