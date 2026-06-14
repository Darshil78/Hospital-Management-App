from extensions import db


class Medicine(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    category = db.Column(
        db.String(100)
    )


    company = db.Column(
        db.String(100)
    )


    quantity = db.Column(
        db.Integer,
        default=0
    )


    price = db.Column(
        db.Float
    )


    expiry_date = db.Column(
        db.String(50)
    )


    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )