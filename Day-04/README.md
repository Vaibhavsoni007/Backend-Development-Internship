# Backend Development Internship - Day 04

## Project Overview

This project is a Flask backend application developed as part of the Backend Development Internship.

The project demonstrates:
- Database design using MySQL
- REST API development using Flask
- Database integration
- File upload handling
- User authentication using bcrypt and JWT
- API security using protected routes

---

## Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Backend programming language |
| Flask | Web framework |
| MySQL | Database management |
| Flask-MySQLdb | Connect Flask with MySQL |
| bcrypt | Password hashing |
| PyJWT | JWT authentication |
| python-dotenv | Manage environment variables |
| Postman | API testing |

---

# Project Setup

## 1. Clone Repository

```bash
git clone <repository_link>
```

Move into project folder:

```bash
cd Day-04
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Database Configuration

Create a `.env` file:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=day04_backend_db

JWT_SECRET_KEY=your_secret_key
```

---

## 5. Run Flask Application

Go to app directory:

```bash
cd app
```

Start server:

```bash
python app.py
```

Server will run on:

```
http://127.0.0.1:5000
```

---

# Database Schema

## Users Table

| Column | Type | Description |
|-------|------|-------------|
| id | INT | User ID |
| username | VARCHAR | Username |
| email | VARCHAR | User email |
| password | VARCHAR | Hashed password |
| role | VARCHAR | User role |
| profile_image | VARCHAR | Uploaded image name |
| created_at | TIMESTAMP | Account creation date |

---

# API Documentation

## 1. Register User

### Endpoint

```
POST /register
```

### Request Body

```json
{
    "username": "Rahul",
    "email": "rahul@gmail.com",
    "password": "123456"
}
```

### Success Response

```json
{
    "message": "User registered successfully with secure password"
}
```

---

## 2. Login User

### Endpoint

```
POST /login
```

### Request Body

```json
{
    "email": "rahul@gmail.com",
    "password": "123456"
}
```

### Success Response

```json
{
    "message": "Login successful",
    "token": "JWT_TOKEN"
}
```

---

## 3. Get All Users (Protected API)

### Endpoint

```
GET /users
```

### Authentication Header

```
Authorization: Bearer JWT_TOKEN
```

### Success Response

```json
[
    {
        "id": 1,
        "username": "Mohan",
        "email": "mohan@gmail.com",
        "role": "user"
    }
]
```

---

## 4. Upload Profile Image

### Endpoint

```
POST /upload/<user_id>
```

Example:

```
POST /upload/1
```

### Body

Select:

```
form-data
```

Add:

| Key | Type |
|-----|------|
| file | File |

### Success Response

```json
{
    "message": "File uploaded successfully",
    "filename": "photo.jpg"
}
```

---

# JWT Authentication Flow

1. Register a user.
2. Login using email and password.
3. Receive JWT token.
4. Add token in request header:

```
Authorization: Bearer YOUR_TOKEN
```

5. Access protected APIs.

---

# Project Structure

```
Day-04
│
├── app
│   ├── app.py            # Flask APIs
│   └── db.py             # Database configuration
│
├── database
│   └── schema.sql        # Database schema
│
├── uploads               # Uploaded images
│
├── .env                  # Environment variables
│
├── requirements.txt      # Project dependencies
│
├── venv                  # Virtual environment
│
└── README.md             # Project documentation
```

---

# Security Features Implemented

- Password hashing using bcrypt
- JWT based authentication
- Protected API routes
- Environment variable protection
- Secure file upload using file validation

---

# Future Improvements

- Role-based authorization (Admin/User)
- Refresh JWT tokens
- Image size validation
- Unique file names for uploads
- API documentation using Swagger

---

# Author

Backend Development Internship - Day 04 Project
