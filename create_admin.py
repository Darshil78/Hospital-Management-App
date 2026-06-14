from app import create_app, db
from models.user import User
from werkzeug.security import generate_password_hash


app=create_app()


with app.app_context():

    admin=User(

        name="Admin",

        email="admin@hospitalms.com",

        password=generate_password_hash("admin123"),

        role="Admin"

    )


    db.session.add(admin)

    db.session.commit()


print("Admin Created")