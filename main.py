from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI()

app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "Student CRUD API is running. Go to /docs to test."}