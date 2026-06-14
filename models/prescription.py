from extensions import db


class Prescription(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    patient_id = db.Column(
        db.Integer,
        db.ForeignKey("patient.id")
    )


    doctor_id = db.Column(
        db.Integer,
        db.ForeignKey("doctor.id")
    )


    medicines = db.Column(
        db.Text
    )

    medicine_name = db.Column(
        db.String(200)
    )

    dosage = db.Column(
        db.String(100)
    )

    timing = db.Column(
        db.String(100)
    )

    meal_instruction = db.Column(
        db.String(100)
    )


    diagnosis = db.Column(
        db.Text
    )


    instructions = db.Column(
        db.Text
    )


    date = db.Column(
        db.String(50)
    )


    patient = db.relationship(
        "Patient"
    )


    doctor = db.relationship(
        "Doctor"
    )