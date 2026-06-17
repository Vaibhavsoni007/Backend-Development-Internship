from flask import Blueprint, request, jsonify
from database.db import mysql
import uuid


certificate_bp = Blueprint("certificate", __name__)


# Generate Certificate API
@certificate_bp.route("/generate-certificate", methods=["POST"])
def generate_certificate():

    data = request.get_json()

    user_name = data.get("user_name")
    course_name = data.get("course_name")

    if not user_name or not course_name:
        return jsonify({
            "error": "All fields are required"
        }), 400


    certificate_id = str(uuid.uuid4())[:8]


    cursor = mysql.connection.cursor()


    query = """
    INSERT INTO certificates
    (user_name, course_name, certificate_id)
    VALUES (%s, %s, %s)
    """


    cursor.execute(
        query,
        (
            user_name,
            course_name,
            certificate_id
        )
    )


    mysql.connection.commit()

    cursor.close()


    return jsonify({
        "message": "Certificate generated successfully",
        "certificate_id": certificate_id
    }), 201



# Get All Certificates API
@certificate_bp.route("/certificates", methods=["GET"])
def get_certificates():

    cursor = mysql.connection.cursor()

    cursor.execute("""
    SELECT * FROM certificates
    """)


    certificates = cursor.fetchall()

    result = []


    for item in certificates:

        result.append({
            "id": item[0],
            "user_name": item[1],
            "course_name": item[2],
            "certificate_id": item[3],
            "generated_at": item[4]
        })


    cursor.close()


    return jsonify(result)