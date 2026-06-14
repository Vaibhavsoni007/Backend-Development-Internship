from flask import Flask
from config import Config
from extensions import db, bcrypt

def create_app():
    from routes.auth_routes import auth_bp

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(auth_bp)

    # Import models here
    from models.user_model import User

    return app


if __name__ == "__main__":

    app = create_app()

    with app.app_context():
        db.create_all()
        print("All tables created successfully!")

    app.run(debug=True)