# Backend Development Internship - Day 05

## Technology Stack

- Python
- Flask
- MySQL
- Flask-MySQLdb
- Bcrypt

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Database Name:

```sql
backend_internship
```

Tables:

- users
- documents
- certificates
- projects

---

# API Endpoints

## Home

### GET /

Response:

```json
Backend Internship Day-05 API Running Successfully
```

---

## Document APIs

### POST /upload

Upload document

### GET /documents

Get all uploaded documents

---

## Authentication APIs

### POST /register

Request:

```json
{
  "username":"Mohan",
  "email":"mohan@gmail.com",
  "password":"123456",
  "role":"admin"
}
```

Response:

```json
{
  "message":"User registered successfully"
}
```

---

### POST /login

Request:

```json
{
  "email":"mohan@gmail.com",
  "password":"123456"
}
```

Response:

```json
{
  "message":"Login successful"
}
```

---

## Role Based Access

### POST /admin

Admin only endpoint

---

## Certificate APIs

### POST /generate-certificate

Request:

```json
{
  "user_name":"Mohan",
  "course_name":"Backend Development Internship"
}
```

---

### GET /certificates

Returns all certificates

---

## Analytics API

### GET /analytics

Returns:

- Total Users
- Total Admins
- Total Documents
- Total Certificates

---

## Project APIs

### POST /projects

Create Project

### GET /projects

Get All Projects

### GET /projects/<id>

Get Single Project

### PUT /projects/<id>

Update Project

### DELETE /projects/<id>

Delete Project

### GET /projects/status/<status>

Search Project By Status

---

# Logging

Log file:

```text
logs/app.log
```

Features:

- Info Logging
- Error Logging
- Global Exception Handling

---

# Database Optimization

Indexes Added:

- users(email)
- documents(file_name)
- certificates(certificate_id)
- projects(status)

---

# Project Features

- Document Upload System
- Authentication System
- Role Based Access Control
- Certificate Generation
- Analytics Dashboard
- Project Management CRUD
- Logging and Error Handling
- Database Optimization
