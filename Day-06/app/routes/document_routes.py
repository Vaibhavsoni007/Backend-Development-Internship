import os
import hashlib

from flask import request, jsonify, send_file
from werkzeug.utils import secure_filename
from app.utils.rbac import role_required
from app.services.storage_service import StorageService
from app.services.cache_service import CacheService


def register_document_routes(app, mysql):

    @app.route("/upload", methods=["POST"])
    def upload_document():

        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400


        file = request.files["file"]


        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400


        filename, filepath = StorageService.save_file(
        file,
        app.config["UPLOAD_FOLDER"]
    )


        # Generate file hash
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256(
                f.read()
            ).hexdigest()


        file_size = os.path.getsize(filepath)


        cursor = mysql.connection.cursor()

        query = """
        INSERT INTO documents
        (filename, original_name, file_type, file_size, file_hash)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                filename,
                file.filename,
                file.content_type,
                file_size,
                file_hash
            )
        )

        mysql.connection.commit()
        CacheService.delete("documents")

        cursor.close()


        return jsonify({
            "message": "Document uploaded successfully",
            "filename": filename,
            "hash": file_hash
        }), 201
    
    @app.route("/documents", methods=["GET"])
    def get_documents():

        cached_documents = CacheService.get("documents")

        if cached_documents:
            return jsonify({
                "source": "cache",
                "data": cached_documents
        }), 200

        cursor = mysql.connection.cursor()

        cursor.execute("""
            SELECT id, original_name, file_type, file_size, upload_date
            FROM documents
            ORDER BY upload_date DESC
        """)

        data = cursor.fetchall()

        documents = []

        for row in data:
            documents.append({
                "id": row[0],
                "name": row[1],
                "type": row[2],
                "size": row[3],
                "uploaded_at": str(row[4])
            })

        cursor.close()

        CacheService.set(
            "documents",
            documents,
            ttl=60
        )

        return jsonify({
            "source": "database",
            "data": documents
        }), 200
    
    @app.route("/download/<int:document_id>", methods=["GET"])
    def download_document(document_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT filename, original_name FROM documents WHERE id=%s",
            (document_id,)
        )

        document = cursor.fetchone()

        cursor.close()

        if not document:
            return jsonify({
            "error": "Document not found"
            }), 404


        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            document[0]
        )

        return send_file(
            filepath,
            as_attachment=True,
            download_name=document[1]
        )
    
    
    @app.route("/document/<int:document_id>", methods=["DELETE"])
    @role_required("admin")
    def delete_document(document_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            "SELECT filename FROM documents WHERE id=%s",
            (document_id,)
        )

        document = cursor.fetchone()

        if not document:
            cursor.close()
            return jsonify({
                "error": "Document not found"
            }), 404


        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            document[0]
        )


        StorageService.delete_file(filepath)


        cursor.execute(
            "DELETE FROM documents WHERE id=%s",
            (document_id,)
        )

        mysql.connection.commit()
        CacheService.delete("documents")

        cursor.close()


        return jsonify({
            "message": "Document deleted successfully"
        }), 200
    
    @app.route("/generate-document", methods=["POST"])
    def generate_document():

        data = request.get_json()

        filename = data.get("filename")
        content = data.get("content")


        if not filename or not content:
            return jsonify({
                "error": "filename and content are required"
            }), 400


        filename = secure_filename(filename) + ".txt"

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )


        with open(filepath, "w") as file:
            file.write(content)


        with open(filepath, "rb") as file:
            file_hash = hashlib.sha256(
                file.read()
            ).hexdigest()


        file_size = os.path.getsize(filepath)


        cursor = mysql.connection.cursor()

        query = """
        INSERT INTO documents
        (filename, original_name, file_type, file_size, file_hash)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                filename,
                filename,
                "text/plain",
                file_size,
                file_hash
            )
        )

        mysql.connection.commit()

        cursor.close()


        return jsonify({
            "message": "Document generated successfully",
            "filename": filename,
            "hash": file_hash
        }), 201
    
    @app.route("/verify-document/<int:document_id>", methods=["GET"])
    def verify_document(document_id):

        cursor = mysql.connection.cursor()

        cursor.execute(
            """
            SELECT filename, file_hash
            FROM documents
            WHERE id = %s
            """,
            (document_id,)
        )

        document = cursor.fetchone()

        cursor.close()


        if not document:
            return jsonify({
                "error": "Document not found"
            }), 404


        filename = document[0]
        stored_hash = document[1]


        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )


        if not os.path.exists(filepath):
            return jsonify({
                "error": "File not found in storage"
            }), 404


        with open(filepath, "rb") as file:
            current_hash = hashlib.sha256(
                file.read()
            ).hexdigest()


        if current_hash == stored_hash:

            return jsonify({
                "message": "Document verified successfully",
                "status": "Valid",
                "hash": current_hash
            }), 200


        return jsonify({
            "message": "Document integrity failed",
            "status": "Invalid",
            "stored_hash": stored_hash,
            "current_hash": current_hash
        }), 400
    
    @app.route("/storage-info", methods=["GET"])
    def storage_info():

        storage = StorageService.get_storage_type(
            app.config
        )

        return jsonify({
            "storage_type": storage,
            "message": "Storage configuration loaded successfully"
        }), 200
    
