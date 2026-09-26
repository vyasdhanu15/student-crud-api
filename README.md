# Student CRUD API

A simple REST API built using **FastAPI** for managing university student records.

The project provides CRUD (Create, Read, Update, Delete) operations for student data and uses **in-memory storage**. No database is required.

## Features

- Create a student
- Get all students
- Get a student by ID
- Update a student
- Delete a student
- Request and response validation using Pydantic
- RESTful HTTP methods and status codes
- Swagger API documentation
- Separate Models, Routes, and Controllers structure

## Project Structure

```text
student-crud-api/
│
├── controllers/
│   └── student_controller.py
│
├── models/
│   └── student_model.py
│
├── routes/
│   └── student_routes.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

| Operation | Method | Endpoint |
|---|---|---|
| Create Student | POST | `/students` |
| Get All Students | GET | `/students` |
| Get Student by ID | GET | `/students/{id}` |
| Update Student | PUT | `/students/{id}` |
| Delete Student | DELETE | `/students/{id}` |

## Student Fields

Each student contains:

- `id` — Unique student ID
- `name` — Student full name
- `email` — Student email address
- `course` — Course/program name
- `semester` — Current semester

## Installation

Clone the repository:

```bash
git clone https://github.com/vyasdhanu15/student-crud-api.git
```

Go into the project directory:

```bash
cd student-crud-api
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test all five CRUD APIs.

## Example Student

```json
{
  "name": "Rahul Patel",
  "email": "rahul@example.com",
  "course": "B.Tech Computer Engineering",
  "semester": 5
}
```

## Storage

This project uses **local in-memory storage** and does not use a database.

Student records are stored while the application is running. Restarting the application resets the stored data.

## Project Deployment

The project is maintained in a public GitHub repository and can be deployed from the Git repository to a hosting platform such as Render.

## Repository

GitHub:

https://github.com/vyasdhanu15/student-crud-api
