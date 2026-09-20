from models.student_model import Student

# Simple in-memory list storage
students_db = []
id_counter = 0

def get_all_students():
    return students_db

def get_student_by_id(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    return None

def create_student(student_data: Student):
    global id_counter
    id_counter += 1
    student_data.id = id_counter
    students_db.append(student_data)
    return student_data

def update_student(student_id: int, student_data: Student):
    for index, student in enumerate(students_db):
        if student.id == student_id:
            student_data.id = student_id
            students_db[index] = student_data
            return student_data
    return None

def delete_student(student_id: int):
    student = get_student_by_id(student_id)
    if student:
        students_db.remove(student)
        return True
    return False