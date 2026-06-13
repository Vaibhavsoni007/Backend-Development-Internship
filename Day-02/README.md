# Student Management REST API

## 📌 Project Overview

This project is a simple Student Management REST API built using Python and Flask.

The API performs CRUD operations (Create, Read, Update, Delete) on student records. It also includes request validation, proper error handling, and API testing using Postman.

---

## 🚀 Features

- Create a new student record
- Get all students data
- Get a single student using ID
- Update student details
- Delete student records
- Input validation
- Proper HTTP status code responses
- API testing using Postman

---

## 🛠️ Technologies Used

- Python
- Flask
- REST API
- JSON
- Postman

---

## 📁 Project Structure

```
Day-02/
│
├── app.py                         # Main Flask application
├── README.md                      # Project overview
├── API_Documentation.md           # Detailed API documentation
├── requirements.txt               # Python dependencies
│
└── Postman_Testing_Screenshots/
    ├── POST_Create_Success.png
    ├── GET_All_Students.png
    ├── GET_Single_Student.png
    ├── PUT_Update_Success.png
    ├── DELETE_Success.png
    └── Error Screenshots
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Move into project folder

```bash
cd Day-02
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python app.py
```

Server will start on:

```
http://127.0.0.1:5000/
```

---

## 🧪 API Testing

All API endpoints were tested using Postman.

The following operations were tested:

- POST - Create student
- GET - Fetch all students
- GET - Fetch single student
- PUT - Update student
- DELETE - Remove student
- Error handling cases

---

## 📄 API Documentation

Detailed API information is available in:

```
API_Documentation.md
```

---

## 🔮 Future Improvements

- Integrate SQLite or MySQL database
- Add authentication and authorization
- Implement advanced validation
- Deploy API on cloud platforms

---

## 👨‍💻 Author

**Vaibhav Soni**

Backend Development Internship Project - Day 02
