from extensions import db


class Patient(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    age = db.Column(
        db.Integer
    )


    gender = db.Column(
        db.String(20)
    )


    blood_group = db.Column(
        db.String(10)
    )


    phone = db.Column(
        db.String(20)
    )


    email = db.Column(
        db.String(120)
    )


    address = db.Column(
        db.String(250)
    )


    disease = db.Column(
        db.String(200)
    )


    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )


    def __repr__(self):

        return self.name