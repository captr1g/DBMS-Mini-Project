from fastapi import HTTPException, status, Depends
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import Schema
from database.models import *
from operator import or_, and_

def Fetch_All(year:int, dept: str, db:Session):
    data = db.query(Student, Teams, Relation, Teacher).join(Relation.student).join(Relation.team_).join(Teams.guide).filter(and_(Student.year == year, Student.dept == dept)).all()
    result = []
    print(data)
    for student in data:
            result.append(
                Schema.Display_student(
                    
                    usn = student[0].usn,
                    name = student[0].name,
                    year = student[0].year,
                    dept = student[0].dept, 
                    team_name = student[1].team_name,
                    guide_name = student[3].name,
                    batch = student[1].batch,
                )
            )
    return result



