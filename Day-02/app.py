from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return "Welcome to Student API"

# create data API
@app.route("/students", methods=["POST"])
def add_student():

    # Get JSON data sent by client
    data = request.get_json()

    # Check if request body is empty
    if not data:
        return jsonify({
            "error": "Request body is empty"
        }), 400

    # Check if all required fields are present
    if "name" not in data or "age" not in data or "course" not in data:
        return jsonify({
            "error": "Name, age and course are required"
        }), 400

    # Check if name is empty
    if data["name"].strip() == "":
        return jsonify({
            "error": "Name cannot be empty"
        }), 400

    # Check if age is invalid
    if data["age"] <= 0:
        return jsonify({
            "error": "Age must be greater than 0"
        }), 400

    # Create student object
    student = {
        "id": len(students) + 1,
        "name": data["name"],
        "age": data["age"],
        "course": data["course"]
    }

    # Save student in list
    students.append(student)

    # Return success response
    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201




# Read data API
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# Read particular data API
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):

    for student in students:
        if student["id"] == id:
            return jsonify(student)

    return jsonify({
        "error": "Student not found"
    }), 404




# update data API
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):

    # Get new data from client
    data = request.get_json()

    # Check empty body
    if not data:
        return jsonify({
            "error": "Request body is empty"
        }), 400

    # Check required fields
    if "name" not in data or "age" not in data or "course" not in data:
        return jsonify({
            "error": "Name, age and course are required"
        }), 400

    # Validate name
    if data["name"].strip() == "":
        return jsonify({
            "error": "Name cannot be empty"
        }), 400

    # Validate age
    if data["age"] <= 0:
        return jsonify({
            "error": "Age must be greater than 0"
        }), 400

    # Find student by ID
    for student in students:

        if student["id"] == id:

            # Update existing data
            student["name"] = data["name"]
            student["age"] = data["age"]
            student["course"] = data["course"]

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            }), 200

    # Student ID not found
    return jsonify({
        "error": "Student not found"
    }), 404






# Delete data API
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    for student in students:

        if student["id"] == id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully"
            }), 200

    return jsonify({
        "error": "Student not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)