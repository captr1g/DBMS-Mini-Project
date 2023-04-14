from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import models, database
from server import Schema, Stud, Authenticate as Auth
from sqlalchemy.orm import Session
from typing import List
from jinja2 import Template

router = APIRouter(prefix = '/student', tags=['Student'])
templates = Jinja2Templates(directory="views")
db = database.get_db

@router.get('/', response_model=List[Schema.Display_student], response_class=HTMLResponse) 
def student(request:Request, year:int, dept:str,db : Session = Depends(db)):
    fetch = Stud.Fetch_All(year, dept, db)
    template = Template(open("views/detail_Students.html").read())
    rendered_template = template.render(data=fetch)
    return HTMLResponse(content=rendered_template)

@router.get('/{filter}')
def student(request:Request,  filter:str=None):
    fetch = Stud.Fetch(filter, db)
    return templates.TemplateResponse('student.html', {'request':request, "data":fetch})
