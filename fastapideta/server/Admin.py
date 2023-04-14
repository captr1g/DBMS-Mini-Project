from fastapi import HTTPException, status, Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import Schema
from database import models
from operator import or_


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash_pass(password:str):
    return pwd_context.hash(password)

def add_user(request: Schema.Add_User, db:Session):
    user = db.query(models.Login).filter(models.Login.username == request.username).first()
    if not user:
        new_user = models.Login(username = request.username, password=  hash_pass(request.password), role= request.role )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        if request.role == "student":
            new_student = models.Student(usn= request.username.lower(), year= request.year, name= request.name, dept= request.dept)
            db.add(new_student)
            db.commit()
            db.refresh(new_student)
            new_marks = models.Marks(usn=request.username.lower(), report = 0, project= 0, viva=0, total=0)
            db.add(new_marks)
            db.commit()
            db.refresh(new_marks)
            return new_student

        elif request.role == "teacher":
            new_teacher = models.Teacher(staff_id= request.username.lower(), name= request.name, dept = request.dept)
            db.add(new_teacher)
            db.commit()
            db.refresh(new_teacher)
            return new_teacher
        
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "user already exists")
