from flask import jsonify


def register_analytics_routes(app, mysql):

    @app.route("/analytics", methods=["GET"])
    def get_analytics():

        cursor = mysql.connection.cursor()

        # Total documents
        cursor.execute(
            "SELECT COUNT(*) FROM documents"
        )
        total_documents = cursor.fetchone()[0]


        # Total users
        cursor.execute(
            "SELECT COUNT(*) FROM users"
        )
        total_users = cursor.fetchone()[0]


        # Total storage used
        cursor.execute(
            """
            SELECT IFNULL(SUM(file_size), 0)
            FROM documents
            """
        )
        total_storage = cursor.fetchone()[0]


        # Documents grouped by type
        cursor.execute(
            """
            SELECT file_type, COUNT(*)
            FROM documents
            GROUP BY file_type
            """
        )

        types = cursor.fetchall()

        document_types = {}

        for item in types:
            document_types[item[0]] = item[1]


        cursor.close()


        return jsonify({
            "total_documents": total_documents,
            "total_users": total_users,
            "total_storage_used_bytes": total_storage,
            "document_types": document_types
        }), 200