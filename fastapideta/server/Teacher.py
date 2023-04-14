from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import models, database
from server import Schema, Teacher, Authenticate as Auth
from sqlalchemy.orm import Session
from operator import or_, and_


def Create_team(data:Schema.add_team, db:Session):
    team = models.Teams(batch=data.batch, team_name=data.team_name, team_guide=data.team_guide)
    db.add(team)
    db.flush()
    relation = models.Relation(usn=data.usn, team=team.team_id)
    db.add(relation)
    db.commit()
    return team

def Create_marks(data:Schema.add_marks, session:Session):
    marks = session.query(models.Marks).filter_by(usn=data.usn).first()
    if data.report != None:
        marks.report = data.report
    if data.project != None:
        marks.project = data.project
    if data.viva != None:
        marks.viva = data.viva
    if (data.viva != None or data.report != None or data.project != None): 
        if data.viva != None:
            marks.total = data.viva+ marks.report + marks.project
        elif data.report != None:
            marks.total = data.report + marks.project + marks.viva
        else:
            marks.total = data.project + marks.viva + marks.report

    session.commit()
    return marks
    # marks = models.Marks(usn=data.usn, report=data.report, project=data.project, viva=data.viva, total= data.report + data.viva + data.project)
    # session.add(marks)
    # session.commit()
    # return marks


def Update(data:Schema.Update , session:Session):
    student = session.query(models.Student).filter_by(usn= data.usn).first()
    relation = session.query(models.Relation).filter_by(usn= data.usn).first()
    teams = session.query(models.Teams).filter_by(team_id=relation.team).first()
    marks = session.query(models.Marks).filter_by(usn=data.usn).first()

    if  data.name != None:
        student.name =  data.name
    if data.year != None:
        student.year = data.year
    if data.dept != None:
        student.dept = data.dept
    if data.batch != None:
        teams.batch = data.batch
    if data.team_name != None:
        teams.team_name = data.team_name
    if data.team_guide != None:
        teams.team_guide = data.team_guide
    if data.report != None:
        marks.report = data.report
    if data.project != None:
        marks.project = data.project
    if data.viva != None:
        marks.viva = data.viva
    if (data.viva != None or data.report != None or data.project != None): 
        if data.viva != None:
            marks.total = data.viva+ marks.report + marks.project
        elif data.report != None:
            marks.total = data.report + marks.project + marks.viva
        else:
            marks.total = data.project + marks.viva + marks.report

    session.commit()
    return data



def Fetch_All(year:int, dept: str, db:Session):
    # data = db.query(models.Student, models.Marks, models.Teams, models.Teacher, models.Relation).join(models.Marks, models.Student.usn == models.Marks.usn).join(and_(models.Teacher.staff_id == models.Teams.team_guide, models.Relation.team == models.Teams.team_id)).join(models.Relation, models.Relation.usn == models.Student.usn).filter(and_(models.Student.year == year, models.Student.dept == dept)).all()
    # data = db.query(models.Student, models.Marks, models.Teams, models.Teacher, models.Relation).join(models.Teams.guide).join(models.Relation.student).join(models.Relation.team_).join(models.Marks.student).filter(and_(models.Student.year == year, models.Student.dept == dept)).all()
    data = db.query(models.Student, models.Marks, models.Teams, models.Teacher, models.Relation).join(models.Marks, models.Student.usn == models.Marks.usn).join(models.Relation, models.Relation.usn == models.Student.usn).join(models.Teams, models.Relation.team == models.Teams.team_id).join(models.Teacher, models.Teacher.staff_id == models.Teams.team_guide).filter(and_(models.Student.year == year, models.Student.dept == dept)).all()

    result = []
    print(data)
    for student in data:
            result.append(
                Schema.Teacher_display_student(
                    usn = student[0].usn,
                    name = student[0].name,
                    year = year, 
                    dept = dept,
                    viva = student[1].viva,
                    report= student[1].report,
                    project = student[1].project,
                    total = student[1].total,
                    team_name = student[2].team_name if student[2].team_name != None else None, 
                    guide_name = student[3].name if student[3].name != None else None,
                    batch = student[2].batch if student[2].batch != None else None
                )
            )
        
    

    return result