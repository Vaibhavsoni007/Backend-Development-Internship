# Backend Development Internship - Day 03

## 📌 Project Overview

This project demonstrates a complete Authentication System using Flask, MySQL, JWT, and Middleware.

Features implemented:
- User Registration
- User Login
- Password Hashing using Bcrypt
- JWT Token Generation
- JWT Authentication Middleware
- Protected API Routes
- MySQL Database Integration
- API Testing using Postman


---

## 🛠 Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- MySQL
- SQLAlchemy ORM
- Flask-Bcrypt
- PyJWT
- Postman


---

## 📁 Project Structure

```
Day-03/
│
├── app.py                  # Main Flask application
├── config.py               # Application configuration
├── extensions.py           # Shared extensions (DB, Bcrypt)
├── .env                    # Environment variables
├── .gitignore              # Files to ignore in Git
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── controllers/
│   └── auth_controller.py  # Register and login logic
│
├── models/
│   └── user_model.py       # Database User model
│
├── routes/
│   └── auth_routes.py      # API endpoints
│
├── middleware/
│   └── auth_middleware.py  # JWT verification middleware
│
├── documentation/
│   └── day03_notes.md      # Learning notes
│
└── screenshots/
    ├── 01_register_success.png
    ├── 02_register_duplicate_email.png
    ├── 03_login_success_token.png
    ├── 04_login_wrong_password.png
    ├── 05_login_wrong_email.png
    ├── 06_profile_without_token.png
    ├── 07_profile_invalid_token.png
    └── 08_profile_valid_token.png
```

---

## ⚙️ Environment Variables

Create a `.env` file and add:

```env
DB_USERNAME=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=backend_day03_db

SECRET_KEY=your_secret_key
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```
git clone <repository-url>
```

### 2. Go to Project Folder

```
cd Day-03
```

### 3. Create Virtual Environment

```
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```
venv\Scripts\activate
```

### 5. Install Dependencies

```
pip install -r requirements.txt
```

### 6. Configure MySQL Database

Create database:

```sql
CREATE DATABASE backend_day03_db;
```

### 7. Run Application

```
python app.py
```

Server will start on:

```
http://127.0.0.1:5000
```

---

# 🔗 API Endpoints


## 1. Register User

**POST**

```
/register
```

Request Body:

```json
{
    "name": "Mohan",
    "email": "mohan@example.com",
    "password": "123456"
}
```

Response:

```json
{
    "message": "User registered successfully"
}
```

---

## 2. Login User

**POST**

```
/login
```

Request:

```json
{
    "email": "mohan@example.com",
    "password": "123456"
}
```

Response:

```json
{
    "message": "Login successful",
    "token": "JWT_TOKEN"
}
```

---

## 3. Get Profile (Protected Route)

**GET**

```
/profile
```

Header:

```
Authorization: Bearer JWT_TOKEN
```

Success Response:

```json
{
    "message": "Welcome to your profile"
}
```

---

## 🔐 Security Features

- Password hashing using Bcrypt
- JWT based authentication
- Token expiration
- Middleware based route protection
- Secure database queries using SQLAlchemy ORM


---

## 📸 API Testing Screenshots

All Postman API testing screenshots are available in the `screenshots` folder.


---

## 📚 Learning Outcomes

After completing this project, I learned:

- Flask project architecture
- Database connection with MySQL
- SQLAlchemy ORM usage
- Authentication and Authorization
- Password hashing techniques
- JWT token generation and validation
- Middleware concepts
- API testing using Postman
- Basic backend security practices


---

## 👨‍💻 Author
vaibhav soni
Created as part of Backend Development Internship - Day 03.
