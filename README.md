# FastAPI — Detailed Learning README

> **Goal:** Learn FastAPI from beginner to production-oriented backend development, especially for AI/ML Engineer projects.
>
> This README focuses on **what, why, how, internal flow, examples, API testing, database integration, project structure, and interview preparation**.

---

# 1. What is FastAPI?

**FastAPI** is a modern Python web framework used to build:

- REST APIs
- Backend services
- Microservices
- AI/ML model APIs
- LLM applications
- RAG backends
- Authentication systems
- Database-backed applications

FastAPI is built around Python type hints and uses:

- **Starlette** → web/HTTP functionality
- **Pydantic** → data validation and serialization
- **Uvicorn** → ASGI server commonly used to run the application

### Simple idea

Without FastAPI:

```text
Frontend
   ↓
??? Python code
   ↓
Database / ML Model
```

With FastAPI:

```text
Frontend
   ↓ HTTP Request
FastAPI
   ↓
Route
   ↓
Service / Business Logic
   ↓
Database / ML Model / LLM
   ↓
Response
   ↓
Frontend
```

---

# 2. Why FastAPI?

For an AI/ML Engineer, FastAPI is especially useful because Python is already used for:

- Machine Learning
- Deep Learning
- Data Science
- LLMs
- LangChain
- RAG
- Model inference

So you can expose your Python model/application through an API.

Example:

```text
React Frontend
      ↓
POST /predict
      ↓
FastAPI
      ↓
ML Model
      ↓
Prediction
      ↓
JSON Response
```

---

# 3. FastAPI vs Flask vs Django

| Feature | FastAPI | Flask | Django |
|---|---|---|---|
| Type | API-focused framework | Lightweight web framework | Full-stack framework |
| Async support | Excellent | Supported | Supported |
| Automatic API docs | Yes | No by default | No by default |
| Validation | Pydantic | Usually external libraries | Django Forms/Serializers depending on stack |
| Learning curve | Easy–Medium | Easy | Medium–Hard |
| AI/ML APIs | Excellent | Good | Good |
| Large full-stack websites | Possible | Possible | Excellent |
| REST API development | Excellent | Good | Excellent with DRF |
| Type hints | Strongly integrated | Optional | Optional |
| Production APIs | Excellent | Excellent | Excellent |

### For your AI/ML Engineer path

FastAPI is a very good choice because you can directly connect:

```text
FastAPI
  ↓
Python
  ↓
ML Model / LangChain / RAG / Agents
  ↓
Database
```

---

# 4. Important Concepts You Must Learn

Learn FastAPI in this order:

```text
1. HTTP basics
2. FastAPI installation
3. First API
4. Routes
5. Path parameters
6. Query parameters
7. Request body
8. Pydantic models
9. Response models
10. CRUD
11. Status codes
12. Error handling
13. Dependency Injection
14. Routers
15. Project structure
16. Middleware
17. CORS
18. Authentication
19. Database
20. SQLAlchemy
21. Async programming
22. File upload
23. Background tasks
24. Testing
25. Deployment
```

---

# 5. HTTP Basics

Before learning FastAPI, understand HTTP.

A client sends a request:

```text
Client
  ↓
HTTP Request
  ↓
Server
```

Server sends:

```text
Server
  ↓
HTTP Response
  ↓
Client
```

A request contains:

```text
Method
URL
Headers
Body
```

Example:

```http
POST /users
Content-Type: application/json

{
    "name": "Arjun",
    "age": 22
}
```

Response:

```http
200 OK

{
    "message": "User created"
}
```

---

# 6. HTTP Methods

## GET

Used to retrieve data.

```http
GET /users
```

Example:

```text
GET /users
→ Get all users
```

---

## POST

Used to create data.

```http
POST /users
```

---

## PUT

Usually used to update an existing resource.

```http
PUT /users/10
```

---

## PATCH

Used for partial updates.

```http
PATCH /users/10
```

Example:

```json
{
    "age": 23
}
```

Only age changes.

---

## DELETE

Used to delete data.

```http
DELETE /users/10
```

---

# 7. HTTP Status Codes

Important status codes:

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

Typical CRUD:

```text
GET     → 200
POST    → 201
PUT     → 200
DELETE  → 204
```

---

# 8. Installation

Create a project:

```bash
mkdir fastapi-project
cd fastapi-project
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

Check:

```bash
pip list
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

Install later:

```bash
pip install -r requirements.txt
```

---

# 9. First FastAPI Application

Create:

```text
main.py
```

Code:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

Run:

```bash
uvicorn main:app --reload
```

Meaning:

```text
uvicorn → server
main    → main.py
app     → FastAPI object
--reload → restart server when code changes
```

---

# 10. Understanding `app = FastAPI()`

```python
from fastapi import FastAPI

app = FastAPI()
```

`FastAPI()` creates your application object.

Routes are then attached to this object:

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

Think:

```text
app
 ├── GET /
 ├── GET /users
 ├── POST /users
 ├── PUT /users/{id}
 └── DELETE /users/{id}
```

---

# 11. Routes / Endpoints

A route connects:

```text
HTTP Method + URL
        ↓
Python Function
```

Example:

```python
@app.get("/users")
def get_users():
    return {
        "users": ["Arjun", "Yash"]
    }
```

Request:

```http
GET /users
```

FastAPI executes:

```python
get_users()
```

Response:

```json
{
    "users": ["Arjun", "Yash"]
}
```

---

# 12. Path Parameters

A path parameter is part of the URL.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
```

Request:

```text
GET /users/10
```

FastAPI receives:

```python
user_id = 10
```

Response:

```json
{
    "user_id": 10
}
```

### Why type annotation matters

```python
user_id: int
```

If the client sends:

```text
/users/abc
```

FastAPI automatically validates it and returns a validation error.

---

# 13. Multiple Path Parameters

```python
@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

URL:

```text
/users/10/posts/50
```

---

# 14. Query Parameters

Query parameters appear after `?`.

Example:

```text
/users?limit=10
```

FastAPI:

```python
@app.get("/users")
def get_users(limit: int = 10):
    return {
        "limit": limit
    }
```

URL:

```text
/users?limit=20
```

Result:

```json
{
    "limit": 20
}
```

---

# 15. Multiple Query Parameters

```python
@app.get("/users")
def get_users(
    limit: int = 10,
    skip: int = 0,
    search: str | None = None
):
    return {
        "limit": limit,
        "skip": skip,
        "search": search
    }
```

Example:

```text
/users?limit=10&skip=20&search=arjun
```

---

# 16. Required vs Optional Query Parameters

Required:

```python
@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}
```

Request:

```text
/search?keyword=python
```

Optional:

```python
@app.get("/search")
def search(keyword: str | None = None):
    return {"keyword": keyword}
```

---

# 17. Request Body

When sending structured data, use a request body.

Example JSON:

```json
{
    "name": "Arjun",
    "age": 22
}
```

Create Pydantic model:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

Route:

```python
@app.post("/users")
def create_user(user: User):
    return user
```

FastAPI automatically:

```text
JSON
 ↓
Pydantic validation
 ↓
Python object
 ↓
Function
```

---

# 18. Pydantic

Pydantic is extremely important in FastAPI.

It is used for:

- Validation
- Serialization
- Request schemas
- Response schemas
- Configuration
- Structured data

Example:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
```

FastAPI expects:

```json
{
    "name": "Arjun",
    "age": 22,
    "email": "arjun@example.com"
}
```

---

# 19. Pydantic Validation

```python
class User(BaseModel):
    name: str
    age: int
```

Invalid:

```json
{
    "name": "Arjun",
    "age": "hello"
}
```

FastAPI/Pydantic detects the invalid input.

This is one of the biggest advantages of FastAPI.

---

# 20. Pydantic Field

You can define constraints:

```python
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=100)
```

Meaning:

```text
name → minimum 2 characters
age  → 18 to 100
```

---

# 21. Nested Pydantic Models

```python
class Address(BaseModel):
    city: str
    state: str


class User(BaseModel):
    name: str
    age: int
    address: Address
```

JSON:

```json
{
    "name": "Arjun",
    "age": 22,
    "address": {
        "city": "Ahmedabad",
        "state": "Gujarat"
    }
}
```

---

# 22. Response Models

Request validation and response validation are separate concepts.

```python
class UserResponse(BaseModel):
    id: int
    name: str


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Arjun",
        "password": "secret"
    }
```

The response model controls what is returned.

This helps prevent accidentally exposing fields.

---

# 23. CRUD

CRUD means:

```text
C → Create
R → Read
U → Update
D → Delete
```

Typical API:

```text
POST   /users
GET    /users
GET    /users/{id}
PUT    /users/{id}
DELETE /users/{id}
```

---

# 24. CRUD Practice with Mock Data

Use this example to practice routes before connecting a database.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


users = {
    1: {
        "name": "Arjun",
        "age": 22,
        "email": "arjun@example.com"
    },
    2: {
        "name": "Yash",
        "age": 22,
        "email": "yash@example.com"
    }
}


# CREATE
@app.post("/users")
def create_user(user: User):
    new_id = max(users.keys()) + 1 if users else 1

    users[new_id] = user.model_dump()

    return {
        "id": new_id,
        "user": users[new_id]
    }


# READ ALL
@app.get("/users")
def get_users():
    return users


# READ ONE
@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[user_id]


# UPDATE
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = user.model_dump()

    return {
        "message": "User updated",
        "user": users[user_id]
    }


# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted",
        "user": deleted_user
    }
```

Run:

```bash
uvicorn main:app --reload
```

---

# 25. Interactive API Documentation

FastAPI automatically generates documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

This is Swagger UI.

You can:

```text
GET
POST
PUT
DELETE
```

directly from the browser.

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 26. Why `/docs` Is Powerful

Suppose you create:

```python
@app.post("/users")
def create_user(user: User):
    ...
```

FastAPI reads:

```python
user: User
```

and Pydantic's schema information.

It automatically generates an OpenAPI specification and interactive docs.

Flow:

```text
Python type hints
       ↓
FastAPI
       ↓
OpenAPI schema
       ↓
Swagger UI
       ↓
/docs
```

---

# 27. HTTPException

Use `HTTPException` when an API request cannot be completed normally.

```python
from fastapi import HTTPException


@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"name": "Arjun"}
```

---

# 28. Custom Status Codes

```python
from fastapi import status


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user(user: User):
    return user
```

This makes the API semantics clearer.

---

# 29. APIRouter

As your application grows, don't put every route in `main.py`.

Bad:

```text
main.py
 ├── 100 routes
 ├── database code
 ├── ML code
 ├── authentication
 └── business logic
```

Better:

```text
main.py
routes/
    users.py
    auth.py
    resume.py
    interview.py
```

Create router:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def get_users():
    return {"users": []}
```

Then in `main.py`:

```python
from fastapi import FastAPI
from routes.users import router as users_router


app = FastAPI()

app.include_router(users_router)
```

---

# 30. Prefixes

You can define:

```python
app.include_router(
    users_router,
    prefix="/api/users"
)
```

Then:

```python
@router.get("/")
def get_users():
    ...
```

becomes:

```text
GET /api/users/
```

---

# 31. Tags

```python
app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)
```

Swagger documentation becomes easier to understand.

---

# 32. Recommended Project Structure

For a real AI/ML application:

```text
project/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── resume.py
│   │   ├── interview.py
│   │   └── matcher.py
│   │
│   ├── services/
│   │   ├── agent1.py
│   │   ├── agent2.py
│   │   ├── agent3.py
│   │   ├── agent4.py
│   │   └── agent5.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── resume.py
│   │   └── interview.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── resume.py
│   │   └── interview.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   └── utils/
│       └── helpers.py
│
├── frontend/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 33. Routes vs Services

This distinction is extremely important.

### Route

Handles HTTP.

```python
@router.post("/resume")
def upload_resume(file):
    ...
```

### Service

Handles actual application logic.

```python
def parse_resume(file):
    ...
```

Architecture:

```text
Frontend
   ↓
Route
   ↓
Service
   ↓
AI / ML / Database
```

Don't put 500 lines of AI logic inside a route.

---

# 34. Example AI/ML API Architecture

Suppose your resume screening system has:

```text
React
  ↓
FastAPI
  ↓
POST /resume/upload
  ↓
resume.py
  ↓
agent1.py
  ↓
Resume Parser
  ↓
Pydantic StructuredResume
```

Then:

```text
POST /resume/upload
POST /interview/start
POST /interview/answer
GET  /interview/result
GET  /candidate/{id}
```

---

# 35. Dependency Injection

FastAPI has a powerful dependency system.

Example:

```python
from fastapi import Depends


def get_current_user():
    return {
        "name": "Arjun"
    }


@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user
```

Flow:

```text
Request
 ↓
FastAPI
 ↓
get_current_user()
 ↓
profile()
 ↓
Response
```

Dependencies are commonly used for:

- Authentication
- Database sessions
- Authorization
- Common parameters
- Shared logic

---

# 36. Database Integration

Typical production flow:

```text
Frontend
   ↓
FastAPI
   ↓
Route
   ↓
Service
   ↓
Database Layer
   ↓
MySQL
```

For Python applications, a common SQL toolkit/ORM is SQLAlchemy.

Install:

```bash
pip install sqlalchemy
```

For MySQL, choose an appropriate MySQL-compatible Python driver.

---

# 37. SQLAlchemy Basic Concept

Instead of writing database queries everywhere, define models.

Conceptually:

```python
class User:
    id
    name
    email
```

Database:

```text
users
-------------------------
id | name | email
-------------------------
1  | Arjun| ...
2  | Yash | ...
```

Application:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
MySQL
```

---

# 38. Database Session

A database session represents a unit of interaction with the database.

Typical pattern:

```python
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
```

Then:

```python
@app.get("/users")
def get_users(db=Depends(get_db)):
    ...
```

Important idea:

```text
Request
 ↓
Open DB session
 ↓
Execute query
 ↓
Return result
 ↓
Close DB session
```

---

# 39. Environment Variables

Never hard-code secrets.

Bad:

```python
DATABASE_PASSWORD = "mypassword"
```

Better:

```text
.env
```

Example:

```env
DATABASE_URL=mysql+driver://username:password@localhost/database
SECRET_KEY=your-secret-key
GROQ_API_KEY=your-api-key
```

Load configuration through environment/configuration management.

Add `.env` to `.gitignore`.

---

# 40. CORS

Suppose:

```text
React
http://localhost:5173

FastAPI
http://localhost:8000
```

Different origins can require CORS configuration.

Install/use FastAPI's CORS middleware:

```python
from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

For production, don't blindly use `*` for trusted frontend origins.

---

# 41. Frontend → FastAPI

React can call:

```text
POST http://localhost:8000/api/resume/upload
```

Conceptually:

```javascript
fetch("http://localhost:8000/api/resume/upload", {
    method: "POST",
    body: formData
});
```

Flow:

```text
React
 ↓ HTTP request
FastAPI endpoint
 ↓
Python service
 ↓
AI/ML model
 ↓
JSON
 ↓
React
```

---

# 42. File Upload

Resume screening requires file uploads.

FastAPI provides `UploadFile`.

Example:

```python
from fastapi import UploadFile, File


@app.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...)
):
    content = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }
```

Install multipart support when needed:

```bash
pip install python-multipart
```

---

# 43. Why `UploadFile`?

`UploadFile` is useful for uploaded files because it provides metadata such as:

```python
file.filename
file.content_type
file.file
```

For large files, this approach is generally preferable to treating the entire upload as a simple string.

---

# 44. Async vs Sync

Normal function:

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

Async function:

```python
@app.get("/")
async def home():
    return {"message": "Hello"}
```

Use `async` when working with asynchronous I/O and async-compatible libraries.

Example:

```python
@app.get("/data")
async def get_data():
    result = await some_async_operation()
    return result
```

Important:

> `async` does not automatically make CPU-heavy ML code faster.

---

# 45. CPU-Bound ML Work

A model performing heavy CPU computation is different from an API waiting for a network response.

Example:

```text
LLM API call
→ mostly waiting for network
→ async can help with concurrency
```

versus:

```text
Huge CPU-heavy model inference
→ CPU/GPU computation
→ async alone does not solve it
```

For heavy workloads, consider:

- worker processes
- task queues
- dedicated inference services
- GPU workers
- background processing

depending on architecture.

---

# 46. Middleware

Middleware sits between request and response processing.

Concept:

```text
Request
 ↓
Middleware
 ↓
Route
 ↓
Middleware
 ↓
Response
```

Common uses:

- CORS
- Logging
- Timing
- Authentication-related processing
- Request IDs

---

# 47. Authentication

Typical API authentication:

```text
Login
 ↓
Verify credentials
 ↓
Create token
 ↓
Client stores token
 ↓
Client sends token
 ↓
FastAPI validates token
 ↓
Protected endpoint
```

JWT is a common token format.

Typical endpoints:

```text
POST /auth/register
POST /auth/login
GET  /users/me
```

Do not store plaintext passwords.

Use a secure password hashing algorithm/library.

---

# 48. Authentication vs Authorization

### Authentication

"Who are you?"

```text
Arjun logged in.
```

### Authorization

"What are you allowed to do?"

```text
Arjun → candidate
HR → recruiter
Admin → administrator
```

Example:

```text
Candidate
→ Can take interview

HR
→ Can view reports

Admin
→ Can manage users
```

---

# 49. Background Tasks

Some tasks don't need to block the immediate response.

Example:

```text
User uploads resume
        ↓
API accepts upload
        ↓
Return response
        ↓
Background processing
```

FastAPI provides `BackgroundTasks` for lightweight background work.

For heavy/reliable distributed jobs, a dedicated task queue is generally more appropriate.

---

# 50. API Versioning

As APIs evolve:

```text
/api/v1/users
/api/v1/resume
```

Later:

```text
/api/v2/users
```

Versioning helps prevent breaking existing clients.

---

# 51. Request Validation Flow

Suppose frontend sends:

```json
{
    "name": "Arjun",
    "age": 22
}
```

Your route:

```python
@app.post("/users")
def create_user(user: User):
    ...
```

Internal conceptual flow:

```text
HTTP Request
     ↓
FastAPI routing
     ↓
Read JSON body
     ↓
Pydantic validation
     ↓
Create User model
     ↓
Call Python function
     ↓
Business logic
     ↓
Response serialization
     ↓
HTTP Response
```

---

# 52. Response Serialization

Python object:

```python
{
    "name": "Arjun",
    "age": 22
}
```

FastAPI converts it into JSON for HTTP response.

Concept:

```text
Python data
   ↓
Serialization
   ↓
JSON
   ↓
HTTP response
```

---

# 53. OpenAPI

FastAPI automatically generates an OpenAPI schema.

OpenAPI describes:

- Endpoints
- HTTP methods
- Request parameters
- Request body
- Response models
- Validation
- Status codes

This is why `/docs` can be generated automatically.

---

# 54. Testing

Install:

```bash
pip install pytest httpx
```

Basic test idea:

```python
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
```

Test API behavior instead of manually testing everything every time.

---

# 55. Testing CRUD

Example:

```python
def test_create_user():

    response = client.post(
        "/users",
        json={
            "name": "Test User",
            "age": 22,
            "email": "test@example.com"
        }
    )

    assert response.status_code == 200
```

Also test:

```text
Valid request
Invalid request
Missing fields
Wrong types
404
Authentication failure
Database errors
```

---

# 56. API Testing Tools

Useful tools:

### Swagger UI

```text
/docs
```

### ReDoc

```text
/redoc
```

### curl

```bash
curl http://127.0.0.1:8000/
```

### Postman

Useful for manually testing API requests.

### Frontend

Eventually test the real:

```text
React → FastAPI
```

flow.

---

# 57. Common API Design

Avoid vague endpoints like:

```text
POST /doSomething
```

Prefer resource-oriented routes:

```text
POST /users
GET /users
GET /users/{id}
PUT /users/{id}
DELETE /users/{id}
```

For your AI project:

```text
POST /resume/upload
POST /interview/start
POST /interview/answer
GET  /interview/{id}/result
```

---

# 58. Error Handling

Don't expose internal secrets/errors to clients.

Bad:

```json
{
    "error": "MySQL password is ..."
}
```

Better:

```json
{
    "detail": "Unable to process request"
}
```

Log the real internal error securely on the server.

---

# 59. Logging

Production applications need logs.

Useful information:

```text
Request received
User ID
Endpoint
Execution time
Error
Status code
```

Avoid logging:

- passwords
- API keys
- tokens
- sensitive personal information

---

# 60. Production Architecture

A basic production architecture can look like:

```text
                 Internet
                    │
                    ▼
              Reverse Proxy
                    │
                    ▼
              FastAPI App
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       MySQL      Redis     AI/ML
                              │
                       LLM / Model
```

Depending on scale:

```text
Frontend
   ↓
Load Balancer
   ↓
FastAPI instances
   ↓
Database
   ↓
Worker / AI services
```

---

# 61. Uvicorn

Uvicorn is an ASGI server commonly used with FastAPI.

Development:

```bash
uvicorn main:app --reload
```

Production deployment often uses multiple worker processes or a process manager/container platform according to the hosting architecture.

---

# 62. ASGI

WSGI is common in traditional Python web applications.

ASGI is designed for modern asynchronous Python applications.

FastAPI is an **ASGI framework**.

Concept:

```text
Client
 ↓
ASGI Server
 ↓
FastAPI
 ↓
Route
```

Uvicorn is an ASGI server.

---

# 63. REST API

REST is an architectural style for APIs.

Example:

```text
/users
```

represents users.

```text
GET /users
```

means retrieve users.

```text
POST /users
```

means create a user.

```text
GET /users/10
```

means retrieve user 10.

---

# 64. Stateless APIs

A typical REST API should avoid depending on server-side request history unless intentionally designed that way.

Each request should contain the information needed to process it, often including an authentication token.

Concept:

```text
Request 1 → independent
Request 2 → independent
Request 3 → independent
```

This makes scaling easier.

---

# 65. Pagination

Suppose database contains:

```text
1,000,000 users
```

Don't return all users.

Use:

```text
GET /users?skip=0&limit=20
```

Concept:

```text
Page 1 → 1–20
Page 2 → 21–40
Page 3 → 41–60
```

---

# 66. Filtering

Example:

```text
GET /users?role=student
```

or:

```text
GET /resumes?skill=python
```

Filtering should be handled intentionally in the service/database layer.

---

# 67. Sorting

Example:

```text
GET /candidates?sort=score
```

Be careful to validate allowed sort fields rather than directly injecting user-provided SQL fragments into queries.

---

# 68. AI/ML Model Endpoint

Suppose you have a trained model:

```python
model.predict(...)
```

Expose it:

```python
class PredictionRequest(BaseModel):
    age: float
    salary: float


@app.post("/predict")
def predict(data: PredictionRequest):

    prediction = model.predict([
        [data.age, data.salary]
    ])

    return {
        "prediction": prediction[0]
    }
```

Architecture:

```text
Frontend
   ↓
POST /predict
   ↓
FastAPI
   ↓
Pydantic validation
   ↓
ML model
   ↓
Prediction
   ↓
JSON
```

---

# 69. LLM API Endpoint

For an AI application:

```python
class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    answer = llm.invoke(request.message)

    return {
        "answer": answer.content
    }
```

Real application:

```text
React
 ↓
POST /chat
 ↓
FastAPI
 ↓
Service
 ↓
LangChain / LLM
 ↓
Response
```

---

# 70. RAG API

Your RAG backend could look like:

```text
POST /documents/upload
        ↓
Parse document
        ↓
Chunk
        ↓
Embedding
        ↓
Vector DB

POST /chat
        ↓
Question
        ↓
Retriever
        ↓
Relevant chunks
        ↓
LLM
        ↓
Answer
```

FastAPI acts as the API layer around this pipeline.

---

# 71. Resume Screening API

For your project:

```text
POST /resume/upload
        ↓
Resume Parser Agent
        ↓
Structured Resume

POST /matcher
        ↓
JD + Resume
        ↓
Matcher Agent
        ↓
Match Score

POST /interview/start
        ↓
Interview Planner

POST /interview/answer
        ↓
Evaluator
        ↓
Next Question

GET /interview/{id}/result
        ↓
Final Report
```

FastAPI is responsible for receiving requests and returning responses.

The actual AI logic should live in services/agents.

---

# 72. Important Separation of Responsibilities

Use:

```text
routes/
→ HTTP/API handling

schemas/
→ Request/response validation

services/
→ Business logic

models/
→ Database models

database/
→ DB connection/session

agents/
→ AI/LLM logic

core/
→ Configuration/security
```

This keeps your code maintainable.

---

# 73. Don't Do This

Avoid:

```python
@app.post("/resume")
def resume(file):

    # 500 lines
    # parse PDF
    # call LLM
    # embeddings
    # database
    # scoring
    # email
    # etc.
```

Instead:

```python
@app.post("/resume")
def resume(file):
    return resume_service.process(file)
```

Then:

```text
route
 ↓
service
 ↓
agent
 ↓
database
```

---

# 74. Common Beginner Mistakes

## Mistake 1 — Everything in `main.py`

Fix:

```text
routes/
services/
schemas/
models/
database/
```

---

## Mistake 2 — No Pydantic models

Bad:

```python
def create_user(data: dict):
```

Better:

```python
def create_user(user: UserCreate):
```

---

## Mistake 3 — Hard-coded secrets

Never:

```python
API_KEY = "..."
```

Use environment variables/secrets management.

---

## Mistake 4 — No error handling

Handle:

```text
404
400
401
403
500
```

appropriately.

---

## Mistake 5 — Mixing database and API logic

Keep DB access separate.

---

## Mistake 6 — Returning sensitive data

Use response models to control output.

---

## Mistake 7 — Using `async` everywhere

Use async when the underlying operations are appropriate for asynchronous execution.

---

# 75. FastAPI Learning Project — Level 1

Build:

```text
User CRUD API
```

Requirements:

```text
POST /users
GET /users
GET /users/{id}
PUT /users/{id}
DELETE /users/{id}
```

Use:

```text
FastAPI
Pydantic
Mock dictionary
Swagger
```

Do not use a database yet.

---

# 76. Level 2 — Database CRUD

Build:

```text
Student Management API
```

Use:

```text
FastAPI
Pydantic
SQLAlchemy
MySQL
```

Endpoints:

```text
POST   /students
GET    /students
GET    /students/{id}
PUT    /students/{id}
DELETE /students/{id}
```

---

# 77. Level 3 — Authentication

Build:

```text
Auth API
```

Features:

```text
Register
Login
Password hashing
JWT
Protected route
Role-based access
```

Roles:

```text
student
faculty
admin
```

---

# 78. Level 4 — ML API

Build:

```text
House Price Prediction API
```

Flow:

```text
Frontend/Postman
 ↓
POST /predict
 ↓
FastAPI
 ↓
Pydantic
 ↓
Scaler
 ↓
ML model
 ↓
Prediction
```

---

# 79. Level 5 — RAG API

Build:

```text
Document Q&A API
```

Endpoints:

```text
POST /documents/upload
POST /chat
GET /documents
```

Stack:

```text
FastAPI
LangChain
Embedding Model
FAISS/Chroma
LLM
```

---

# 80. Level 6 — Your Main Project

Build:

```text
AI Resume Screening + Interview System
```

Possible API:

```text
POST /api/resume/upload
POST /api/resume/parse
POST /api/matcher/run
POST /api/interview/start
POST /api/interview/answer
GET  /api/interview/{id}/result
GET  /api/candidates
```

Architecture:

```text
                  React
                    │
                    │ HTTP
                    ▼
                FastAPI
                    │
             ┌──────┴──────┐
             ▼             ▼
          Routes         Auth
             │
             ▼
          Services
             │
      ┌──────┼──────────┐
      ▼      ▼          ▼
   Agents   DB        Storage
      │      │
      ▼      ▼
     LLM    MySQL
```

---

# 81. What Happens When Frontend Calls an API?

Example:

```text
React
```

sends:

```http
POST /api/interview/answer
```

with:

```json
{
    "interview_id": 10,
    "answer": "My answer..."
}
```

FastAPI:

```text
1. Receives HTTP request
2. Finds matching route
3. Validates request body
4. Executes route
5. Calls service
6. Service calls evaluator/agent
7. Database is updated
8. Response model is created
9. JSON response is returned
```

---

# 82. Environment Setup Cheat Sheet

### Create project

```bash
mkdir project
cd project
```

### Create venv

```bash
python3 -m venv .venv
```

### Activate

```bash
source .venv/bin/activate
```

### Deactivate

```bash
deactivate
```

### Install

```bash
pip install fastapi uvicorn
```

### Save requirements

```bash
pip freeze > requirements.txt
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run

```bash
uvicorn main:app --reload
```

### Check Python

```bash
python3 --version
```

### Check pip

```bash
pip --version
```

---

# 83. Useful Development Commands

Run on another port:

```bash
uvicorn main:app --reload --port 8001
```

Bind to all interfaces:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Development URL:

```text
http://127.0.0.1:8000
```

Docs:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 84. Recommended Learning Order for You

Since you are targeting AI/ML Engineering, don't spend months learning every advanced FastAPI feature.

### Phase 1 — Fundamentals

Learn deeply:

```text
FastAPI app
Routes
GET
POST
PUT
DELETE
Path params
Query params
Request body
Pydantic
Response models
HTTPException
Status codes
Swagger
```

### Phase 2 — Real Backend

Then:

```text
APIRouter
Project structure
Dependency Injection
CORS
Environment variables
File uploads
Authentication
```

### Phase 3 — Database

Then:

```text
SQL
MySQL
SQLAlchemy
Models
CRUD
Sessions
Relationships
Transactions
Migrations
```

### Phase 4 — Production

Then:

```text
Testing
Logging
Middleware
Async
Docker
Deployment
Security
API versioning
```

### Phase 5 — AI Integration

Finally:

```text
FastAPI
 ↓
LangChain
 ↓
RAG
 ↓
Agents
 ↓
LLM
 ↓
Vector DB
 ↓
MySQL
```

---

# 85. FastAPI Interview Questions

## Beginner

### Q1. What is FastAPI?

**Answer:**

FastAPI is a modern Python web framework designed primarily for building APIs. It uses Python type hints for validation and integrates Pydantic for data validation and serialization.

---

### Q2. Why is FastAPI popular for AI/ML applications?

**Answer:**

Because AI/ML applications are commonly built in Python. FastAPI makes it easy to expose ML models, LLM pipelines, RAG systems, and AI services through REST APIs.

---

### Q3. What is an endpoint?

**Answer:**

An endpoint is a specific URL and HTTP method through which a client interacts with a backend service.

Example:

```text
GET /users
```

---

### Q4. What is Pydantic?

**Answer:**

Pydantic is used to define structured data models and validate incoming and outgoing data using Python type annotations.

---

### Q5. What is Uvicorn?

**Answer:**

Uvicorn is an ASGI server commonly used to run FastAPI applications.

---

# 86. Intermediate Interview Questions

### Q1. Difference between path and query parameters?

Path:

```text
/users/10
```

Query:

```text
/users?limit=10
```

Path parameters usually identify a specific resource, while query parameters commonly control filtering, pagination, searching, or optional behavior.

---

### Q2. What is `Depends()`?

`Depends()` is FastAPI's dependency injection mechanism.

It is commonly used for:

```text
Database sessions
Authentication
Authorization
Reusable logic
```

---

### Q3. What is `APIRouter`?

`APIRouter` allows routes to be grouped into separate modules.

This makes large FastAPI applications easier to maintain.

---

### Q4. What is middleware?

Middleware is logic that can run around request/response processing.

Common uses include:

```text
CORS
Logging
Request timing
Request IDs
```

---

### Q5. What is CORS?

CORS controls whether browser-based clients from one origin are allowed to access resources from another origin.

---

# 87. Advanced Interview Questions

### Q1. FastAPI vs Flask?

Key differences:

```text
FastAPI → ASGI, type-hint-driven validation, automatic OpenAPI docs
Flask   → lightweight WSGI-oriented framework with a broad extension ecosystem
```

---

### Q2. What is ASGI?

ASGI is the interface specification for asynchronous-capable Python web applications and servers.

FastAPI is built for ASGI.

---

### Q3. Does async make ML inference faster?

No.

`async` mainly helps with concurrency for suitable I/O-bound operations. CPU/GPU-heavy model inference requires appropriate compute and architecture.

---

### Q4. How would you deploy an ML model using FastAPI?

Example:

```text
Client
 ↓
Reverse Proxy / Load Balancer
 ↓
FastAPI
 ↓
Validation
 ↓
Model Service
 ↓
Prediction
 ↓
JSON
```

For larger systems, inference can be separated into dedicated worker/model services.

---

### Q5. How would you structure a production AI backend?

Example:

```text
routes
services
schemas
models
database
agents
core
utils
```

Routes handle HTTP concerns while services and AI modules handle business/application logic.

---

# 88. FastAPI Mental Model

Remember this:

```text
                 CLIENT
                    │
                    ▼
              HTTP REQUEST
                    │
                    ▼
              FASTAPI ROUTER
                    │
                    ▼
             VALIDATION
             (Pydantic)
                    │
                    ▼
                 ROUTE
                    │
                    ▼
                SERVICE
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
     DATABASE      ML          LLM
        │           │           │
        └───────────┼───────────┘
                    ▼
                RESPONSE
                    │
                    ▼
                  JSON
                    │
                    ▼
                 CLIENT
```

If you understand this flow, you understand the core of FastAPI backend development.

---

# 89. Most Important Topics Checklist

Use this checklist:

- [ ] What is FastAPI?
- [ ] HTTP request/response
- [ ] GET
- [ ] POST
- [ ] PUT
- [ ] PATCH
- [ ] DELETE
- [ ] Status codes
- [ ] Path parameters
- [ ] Query parameters
- [ ] Request body
- [ ] Pydantic
- [ ] Field validation
- [ ] Response models
- [ ] HTTPException
- [ ] Swagger
- [ ] OpenAPI
- [ ] APIRouter
- [ ] Dependency Injection
- [ ] CORS
- [ ] Middleware
- [ ] File Upload
- [ ] Environment variables
- [ ] Authentication
- [ ] JWT
- [ ] Authorization
- [ ] MySQL
- [ ] SQLAlchemy
- [ ] Database sessions
- [ ] CRUD with DB
- [ ] Async/await
- [ ] Testing
- [ ] Logging
- [ ] Docker
- [ ] Deployment
- [ ] AI/ML model serving
- [ ] LLM API
- [ ] RAG API
- [ ] Production architecture

---

# 90. Final Learning Strategy

For an AI/ML Engineer, learn FastAPI **by building**, not only by watching tutorials.

Recommended sequence:

```text
Step 1
↓
Hello World API

Step 2
↓
GET + POST

Step 3
↓
PUT + DELETE

Step 4
↓
Pydantic validation

Step 5
↓
CRUD with mock data

Step 6
↓
Split routes using APIRouter

Step 7
↓
MySQL + SQLAlchemy

Step 8
↓
Authentication

Step 9
↓
React → FastAPI

Step 10
↓
ML model → FastAPI

Step 11
↓
LangChain → FastAPI

Step 12
↓
RAG → FastAPI

Step 13
↓
Your Resume Screening System
```

### The key idea

Don't try to become a pure backend specialist before building AI systems.

Your target stack can be:

```text
Python
   +
FastAPI
   +
MySQL
   +
LangChain
   +
RAG
   +
Agents
   +
LLMs
   +
ML
   +
React
```

FastAPI becomes the **bridge between your AI/ML logic and the frontend/client**.

---

# Quick Reference

## Basic API

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

Run:

```bash
uvicorn main:app --reload
```

Docs:

```text
http://127.0.0.1:8000/docs
```

## Request model

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

## POST

```python
@app.post("/users")
def create_user(user: User):
    return user
```

## Error

```python
raise HTTPException(
    status_code=404,
    detail="Not found"
)
```

## Dependency

```python
@app.get("/profile")
def profile(user=Depends(get_current_user)):
    return user
```

---

# Conclusion

FastAPI is not just a way to create simple Python endpoints.

For an AI/ML Engineer, it can serve as the **backend/API layer around ML models, LLM applications, RAG pipelines, agents, databases, authentication, and frontend applications**.

The most important architecture to remember is:

```text
Frontend
   ↓
HTTP
   ↓
FastAPI Route
   ↓
Pydantic Validation
   ↓
Service Layer
   ↓
AI / ML / Database
   ↓
Response Model
   ↓
JSON
   ↓
Frontend
```

Master this flow first. Then progressively add databases, authentication, AI services, testing, and deployment.
