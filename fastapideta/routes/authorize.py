from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import models, database
from server import Schema, Authenticate as Auth
from sqlalchemy.orm import Session

router = APIRouter(tags=['Authentication'])
templates = Jinja2Templates(directory="views")
db = database.get_db

@router.get('/login', response_class=HTMLResponse)
def load_login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post('/login', response_model=Schema.Token, status_code=status.HTTP_200_OK)
def user_login(request:OAuth2PasswordRequestForm = Depends(), db : Session = Depends(db)):
    access_token = Auth.Login(request, db)
    return access_token