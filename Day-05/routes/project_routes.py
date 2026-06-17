from flask import Blueprint, request, jsonify
from database.db import mysql


project_bp = Blueprint("project", __name__)


# CREATE Project
@project_bp.route("/projects", methods=["POST"])
def create_project():

    data = request.get_json()

    project_name = data.get("project_name")
    description = data.get("description")
    status = data.get("status", "Pending")


    if not project_name:
        return jsonify({
            "error": "Project name is required"
        }), 400


    cursor = mysql.connection.cursor()

    query = """
    INSERT INTO projects(project_name, description, status)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (project_name, description, status)
    )

    mysql.connection.commit()
    cursor.close()


    return jsonify({
        "message": "Project created successfully"
    }), 201



# READ All Projects
@project_bp.route("/projects", methods=["GET"])
def get_projects():

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM projects"
    )

    projects = cursor.fetchall()

    cursor.close()


    result = []

    for project in projects:
        result.append({
            "id": project[0],
            "project_name": project[1],
            "description": project[2],
            "status": project[3],
            "created_at": project[4]
        })


    return jsonify(result)



# READ Single Project
@project_bp.route("/projects/<int:id>", methods=["GET"])
def get_project(id):

    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT * FROM projects WHERE id=%s",
        (id,)
    )

    project = cursor.fetchone()

    cursor.close()


    if not project:
        return jsonify({
            "error": "Project not found"
        }), 404


    return jsonify({
        "id": project[0],
        "project_name": project[1],
        "description": project[2],
        "status": project[3],
        "created_at": project[4]
    })



# UPDATE Project
@project_bp.route("/projects/<int:id>", methods=["PUT"])
def update_project(id):

    data = request.get_json()

    project_name = data.get("project_name")
    description = data.get("description")
    status = data.get("status")


    cursor = mysql.connection.cursor()


    query = """
    UPDATE projects
    SET project_name=%s,
        description=%s,
        status=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (
            project_name,
            description,
            status,
            id
        )
    )


    mysql.connection.commit()
    cursor.close()


    return jsonify({
        "message": "Project updated successfully"
    })



# DELETE Project
@project_bp.route("/projects/<int:id>", methods=["DELETE"])
def delete_project(id):

    cursor = mysql.connection.cursor()

    cursor.execute(
        "DELETE FROM projects WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()
    cursor.close()


    return jsonify({
        "message": "Project deleted successfully"
    })

# Search projects by status
@project_bp.route("/projects/status/<status>", methods=["GET"])
def get_project_by_status(status):

    cursor = mysql.connection.cursor()

    query = """
    SELECT * FROM projects
    WHERE status = %s
    """

    cursor.execute(query, (status,))

    projects = cursor.fetchall()

    cursor.close()


    result = []


    for project in projects:
        result.append({
            "id": project[0],
            "project_name": project[1],
            "description": project[2],
            "status": project[3],
            "created_at": project[4]
        })


    return jsonify(result)