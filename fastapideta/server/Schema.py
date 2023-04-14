from pydantic import BaseModel
from typing import List

class Token(BaseModel):
    access_token : str
    token_type : str
    user : str
    class Config():
        orm_mode = True

class UserData(BaseModel):
    username : str
    user : str
    class Config():
        orm_mode = True

class Add_User(BaseModel):
    username : str
    name : str
    dept : str
    year : int = None
    role : str
    password : str
    class Config():
        orm_mode = True

class Display_student(BaseModel):
    usn : str
    name : str
    year : int 
    dept : str
    team_name : str
    guide_name : str
    batch:str
    class Config():
        orm_mode = True

class Teacher_display_student(BaseModel):
    usn : str
    name : str
    year : int 
    dept : str
    team_name : str = None
    guide_name : str = None
    batch:str = None
    viva:int
    report: int
    project:int
    total : int
    class Config():
        orm_mode = True

class Update(BaseModel):
    usn : str 
    name : str = None
    year : int = None
    dept : str= None
    team_name : str= None
    team_guide : str= None
    batch: int = None
    viva : int = None
    report: int = None
    project:int = None
    class Config():
        orm_mode = True


class add_team(BaseModel):
    usn : str
    batch : int 
    team_name : str
    team_guide: str
    class Config():
        orm_mode = True

class add_marks(BaseModel):
    usn : str
    viva: int
    report: int
    project: int
    class Config():
        orm_mode = True