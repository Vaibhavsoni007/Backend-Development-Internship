from flask import Blueprint, jsonify
from database.db import mysql


analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics", methods=["GET"])
def get_analytics():

    cursor = mysql.connection.cursor()

    # Total users
    cursor.execute("""
        SELECT COUNT(*) FROM users
    """)
    total_users = cursor.fetchone()[0]


    # Total admins
    cursor.execute("""
        SELECT COUNT(*) FROM users
        WHERE role = 'admin'
    """)
    total_admins = cursor.fetchone()[0]


    # Total normal users
    cursor.execute("""
        SELECT COUNT(*) FROM users
        WHERE role = 'user'
    """)
    total_users_normal = cursor.fetchone()[0]


    # Total documents
    cursor.execute("""
        SELECT COUNT(*) FROM documents
    """)
    total_documents = cursor.fetchone()[0]


    # Total certificates
    cursor.execute("""
        SELECT COUNT(*) FROM certificates
    """)
    total_certificates = cursor.fetchone()[0]


    cursor.close()


    return jsonify({
        "total_users": total_users,
        "total_admins": total_admins,
        "total_normal_users": total_users_normal,
        "total_documents": total_documents,
        "total_certificates": total_certificates
    })