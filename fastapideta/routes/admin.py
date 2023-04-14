from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import models, database
from server import Schema, Admin, Authenticate as Auth
from sqlalchemy.orm import Session

router = APIRouter(prefix = '/admin', tags=['Admin'])
templates = Jinja2Templates(directory="views")
db = database.get_db

@router.get('/', response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@router.post('/add')
def signup(request: Schema.Add_User, db:Session=Depends(db)):
        new_user = Admin.add_user(request, db)
        
