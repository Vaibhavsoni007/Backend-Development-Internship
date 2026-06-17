from flask import Flask
from config import Config
from database.db import mysql
from routes.document_routes import document_bp
from routes.auth_routes import auth_bp
from routes.certificate_routes import certificate_bp
from routes.analytics_routes import analytics_bp
from routes.project_routes import project_bp
from logs.logger import logger

app = Flask(__name__)

app.config.from_object(Config)

mysql.init_app(app)

app.register_blueprint(document_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(certificate_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(project_bp)


@app.route("/")
def home():

    logger.info("Home API accessed")

    return "Backend Internship Day-05 API Running Successfully"

@app.errorhandler(Exception)
def handle_exception(error):

    logger.error(
        f"Unexpected Error: {str(error)}"
    )

    return {
        "error": "Internal Server Error"
    }, 500




if __name__ == "__main__":
    app.run(debug=True)