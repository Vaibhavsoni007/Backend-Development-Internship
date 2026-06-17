from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

from database.db import mysql


document_bp = Blueprint("document", __name__)


ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Upload API
@document_bp.route("/upload", methods=["POST"])
def upload_document():

    if "file" not in request.files:
        return jsonify({
            "error": "No file selected"
        }), 400


    file = request.files["file"]


    if file.filename == "":
        return jsonify({
            "error": "Empty filename"
        }), 400


    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)

        path = os.path.join("uploads", filename)

        file.save(path)


        cursor = mysql.connection.cursor()


        query = """
        INSERT INTO documents(file_name, file_path)
        VALUES (%s, %s)
        """

        cursor.execute(query, (filename, path))

        mysql.connection.commit()

        cursor.close()


        return jsonify({
            "message": "File uploaded successfully",
            "file": filename
        }), 201


    return jsonify({
        "error": "Only PDF, JPG, JPEG and PNG files allowed"
    }), 400



# Get all documents
@document_bp.route("/documents", methods=["GET"])
def get_documents():

    cursor = mysql.connection.cursor()

    cursor.execute("""
    SELECT * FROM documents
    """)


    data = cursor.fetchall()


    documents = []


    for item in data:
        documents.append({
            "id": item[0],
            "file_name": item[1],
            "file_path": item[2],
            "uploaded_at": item[3]
        })


    cursor.close()


    return jsonify(documents)