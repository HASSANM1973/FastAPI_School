
from fastapi import FastAPI
from pydantic import BaseModel

# creat Fast API
app=FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_cordentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Identfai Bassmodel by pydantic
class student(BaseModel):
    id:int
    name:str
    grade:int

# creat list to save data in memory     
students=[student(id=1, name="karim ali",grade=5),
          student(id=2, name="kadija ahmed",grade=3),
          ]
# read all data 
@app.get("/students/")
def read_students():
    return students

# Add New data 
@app.post("/students/")
def create_student(New_Student:student):
    students.append(New_Student)
    return New_Student

# Update data by useing (ID) PUT Methode
@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:student):
    for index,student in enumerate(students):
        if student.id == student_id:
            students[index]=updated_student
            return updated_student
    return{"error":" Student not found"}

# Delet method to delete data by useing (ID)
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id==student_id:
           del students[index]
           return{"message":"Student deleted"} 
    return{"error":" Student not found"} 
 
        
            