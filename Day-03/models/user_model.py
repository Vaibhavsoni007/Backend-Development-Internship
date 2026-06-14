from extensions import db
from datetime import datetime


class User(db.Model):

    __tablename__ = "users"

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # User Name
    name = db.Column(
        db.String(100),
        nullable=False
    )

    # User Email
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    # Hashed Password
    password = db.Column(
        db.String(255),
        nullable=False
    )

    # Account Creation Time
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


    def __repr__(self):
        return f"<User {self.email}>"