from extensions import db


class Appointment(db.Model):

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


    appointment_date = db.Column(
        db.String(50)
    )


    appointment_time = db.Column(
        db.String(50)
    )


    reason = db.Column(
        db.Text
    )

    visited_before = db.Column(
        db.Boolean,
        default=False
    )

    old_report = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(30),
        default="Pending"
    )


    patient = db.relationship(
        "Patient",
        backref="appointments"
    )


    doctor = db.relationship(
        "Doctor",
        backref="appointments"
    )


    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )