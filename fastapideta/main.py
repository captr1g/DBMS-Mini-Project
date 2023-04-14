from fastapi import FastAPI, Request, status, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from server import Schema, Stud, Authenticate as Auth
from database import models, database as db
from routes import authorize, admin, student, teacher
from sqlalchemy.orm import Session

models.db.Base.metadata.create_all(db.engine)
templates = Jinja2Templates("views")
db1 = db.get_db
app = FastAPI(
    title="Alumni (Student Project Management System) ",
    description="18CSL58 DBMS Laboratory Mini Project on Student Project Management System",
    version="2.1.0",
    # swagger_ui_oauth2_redirect_url='/login',
    contact={
        "Developer 1": {
            "Name" : "Yash Raj Saxena",
            "USN"  : "1HK20CS183",
            "Mail" : "1hk20cs183@hkbk.edu.in",
            "Role" : "Backend Engineer"
        },
        "Developer 2": {
            "Name" : "Vidya Kumari" ,
            "USN"  : "1HK20CS189",
            "Mail" : "1hk20cs189@hkbk.edu.in",
            "Role" : "Frontend Designer"
        }
    }
)
app.include_router(authorize.router)
app.include_router(admin.router)
app.include_router(student.router)
app.include_router(teacher.router)

@app.get('/', response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get('/search', response_class=HTMLResponse)
def root(request:Request):
    return templates.TemplateResponse("search.html", {"request": request})

