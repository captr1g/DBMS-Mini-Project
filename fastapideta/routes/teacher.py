from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import models, database
from server import Schema, Teacher, Authenticate as Auth
from sqlalchemy.orm import Session
from typing import List, Dict
from jinja2 import Template

router = APIRouter(prefix = '/teacher', tags=['Teacher'])
templates = Jinja2Templates(directory="views")
db = database.get_db


@router.get('/', response_model=List[Schema.Teacher_display_student]) 
def all_student(request:Request, year:int, dept:str, db : Session = Depends(db)):
    fetch = Teacher.Fetch_All(year, dept, db)
    template = Template(open("views/detail_Teacher.html").read())
    rendered_template = template.render(data=fetch)
    return HTMLResponse(content=rendered_template)

    

@router.get('/{filter}')
def filter_Students(request:Request,  filter:str=None):
    fetch = Teacher.Fetch(filter, db)
    return templates.TemplateResponse('student.html', {'request':request, "data":fetch})

@router.post('/add-team')
def add_team(request:Schema.add_team, db:Session= Depends(db)):
    # data = request.json()
    teacher = Teacher.Create_team(request, db)
    return teacher
    
@router.post('/add-mark')
def add_team(request:Schema.add_marks, db:Session= Depends(db)):
    # data = request.json()
    teacher = Teacher.Create_marks(request, db)
    return teacher

@router.put('/update')
def update_marks(request:Schema.Update, db : Session = Depends(db)):
    # data = request.json()
    Marks = Teacher.Update(request, db)
    return Marks

# @router.delete('/teams/{id}')
# def delete_teams(request:Request,  id:int):
#     Team = Teacher.delete_team(id, db)
#     return Team