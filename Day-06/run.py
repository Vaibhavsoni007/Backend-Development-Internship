from flask import Flask
from flask_mysqldb import MySQL

from app.config import Config
from app.routes.document_routes import register_document_routes
from flask_jwt_extended import JWTManager
from app.routes.auth_routes import register_auth_routes
from app.routes.analytics_routes import register_analytics_routes
from app.routes.job_routes import register_job_routes


from app.extensions import limiter


app = Flask(__name__)

app.config.from_object(Config)

limiter.init_app(app)

mysql = MySQL(app)

jwt = JWTManager(app)

register_document_routes(app, mysql)
register_auth_routes(app, mysql)
register_analytics_routes(app, mysql)
register_job_routes(app)



@app.route("/")
def home():
    return {
        "message": "Document Management API Running Successfully",
        "database": "Connected Successfully"
    }


if __name__ == "__main__":
    app.run(debug=True)