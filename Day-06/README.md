# Document Management Backend System

## Technologies Used

- Python
- Flask
- MySQL
- JWT Authentication
- Flask Limiter
- Multithreading

## Features

### Document Management
- Upload documents
- Download documents
- Delete documents
- Generate documents
- Verify document integrity

### Security
- Password hashing
- JWT authentication
- Role Based Access Control
- API rate limiting

### Performance
- In-memory caching
- Database indexing
- Optimized queries

### Advanced Features
- Analytics APIs
- Background job processing
- Scalable storage architecture

## Project Structure

app/
├── routes/
├── services/
├── config.py
├── extensions.py

## APIs

- POST /upload
- GET /documents
- GET /download/<id>
- DELETE /document/<id>
- POST /login
- POST /register
- GET /analytics
- POST /process-document/<id>
- GET /job-status/<id>
