# Student Management REST API Documentation

## 1. Project Overview

This project is a simple Student Management REST API built using Python and Flask.

It allows users to perform CRUD operations on student records.

The API includes:
- Create a new student
- Read all students
- Read a specific student by ID
- Update student information
- Delete a student
- Request validation
- Proper error handling

---

## 2. Technologies Used

- Python
- Flask
- REST API
- JSON
- Postman (for API testing)

---

## 3. Base URL

http://127.0.0.1:5000/

---

# 4. API Endpoints

## 4.1 Home API

### Endpoint

GET /

### Description

Checks whether the backend server is running.

### Success Response

Status Code: 200 OK

```json
{
    "message": "Welcome to Student API"
}


Create Student API

Endpoint

POST /students

Description

Adds a new student record.

Request Body
{
    "name": "Mohan",
    "age": 21,
    "course": "B.Tech"
}
Success Response

Status Code: 201 Created

{
    "message": "Student added successfully",
    "student": {
        "id": 1,
        "name": "Mohan",
        "age": 21,
        "course": "B.Tech"
    }
}
Error Responses
Empty request body

Status Code: 400 Bad Request

{
    "error": "Request body is empty"
}
Missing fields

Status Code: 400 Bad Request

{
    "error": "Name, age and course are required"
}

Get All Students API
Endpoint

GET /students

Description

Returns the list of all students.

Success Response

Status Code: 200 OK

[
    {
        "id": 1,
        "name": "Mohan",
        "age": 21,
        "course": "B.Tech"
    }
]

Get Single Student API
Endpoint

GET /students/1

Description

Returns the details of a particular student based on ID.

Success Response

Status Code: 200 OK

{
    "id": 1,
    "name": "Mohan",
    "age": 21,
    "course": "B.Tech"
}
Error Response

Status Code: 404 Not Found

{
    "error": "Student not found"
}

Update Student API
Endpoint

PUT /students/1

Description

Updates an existing student's information.

Request Body
{
    "name": "Rohan",
    "age": 22,
    "course": "BCA"
}
Success Response

Status Code: 200 OK

{
    "message": "Student updated successfully",
    "student": {
        "id": 1,
        "name": "Rohan",
        "age": 22,
        "course": "BCA"
    }
}
Error Responses

400 Bad Request

{
    "error": "Invalid or missing data"
}

404 Not Found

{
    "error": "Student not found"
}

Delete Student API
Endpoint

DELETE /students/1

Description

Deletes a student record using ID.

Success Response

Status Code: 200 OK

{
    "message": "Student deleted successfully"
}
Error Response

Status Code: 404 Not Found

{
    "error": "Student not found"
}


HTTP Status Codes Used
Status Code	Meaning
200	Request successful
201	Resource created successfully
400	Bad request or invalid input
404	Resource not found