Backend Development - Day 03

Topics Covered:

1. Authentication
- User identity verification
- Implemented using Login API

2. Authorization
- Checking user permissions
- Implemented using protected routes

3. JWT
- JSON Web Token
- Used for stateless authentication

4. Password Security
- Passwords are stored using Bcrypt hashing

5. Middleware
- Used to check JWT before accessing private APIs

6. Database
- MySQL connected using SQLAlchemy ORM

APIs Created:

POST /register
- Creates a new user

POST /login
- Authenticates user and generates JWT token

GET /profile
- Protected route requiring JWT token