from fastapi import APIRouter, Response, status
from models.student_model import Student
from controllers import student_controller

router = APIRouter()

@router.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    new_student = student_controller.create_student(student)
    return {"isSuccess": True, "message": "Student created successfully", "student": new_student}

@router.get("/students")
def get_students(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"isSuccess": True, "students": student_controller.get_all_students()}

@router.get("/students/{student_id}")
def get_student(student_id: int, response: Response):
    student = student_controller.get_student_by_id(student_id)
    if not student:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"isSuccess": False, "message": "Student not found"}
    
    response.status_code = status.HTTP_200_OK
    return {"isSuccess": True, "student": student}

@router.put("/students/{student_id}")
def update_student(student_id: int, student_data: Student, response: Response):
    updated = student_controller.update_student(student_id, student_data)
    if not updated:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"isSuccess": False, "message": "Student not found"}
    
    response.status_code = status.HTTP_200_OK
    return {"isSuccess": True, "message": "Student updated successfully", "student": updated}

@router.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, response: Response):
    success = student_controller.delete_student(student_id)
    if not success:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"isSuccess": False, "message": "Student not found"}
    return None