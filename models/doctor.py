from extensions import db


class Doctor(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    specialization = db.Column(
        db.String(100)
    )


    qualification = db.Column(
        db.String(150)
    )


    experience = db.Column(
        db.Integer
    )


    phone = db.Column(
        db.String(20)
    )


    email = db.Column(
        db.String(120)
    )


    available_time = db.Column(
        db.String(100)
    )


    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )


    def __repr__(self):

        return self.name