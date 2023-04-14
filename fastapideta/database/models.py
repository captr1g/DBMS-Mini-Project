from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from . import database as db


class Login(db.Base):
    __tablename__ = 'login'
    username = Column(String(55), primary_key=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(10), nullable=False)

class Student(db.Base):
    __tablename__ ='student'
    usn = Column(String(10), ForeignKey('login.username', ondelete='CASCADE'), primary_key=True, nullable=False)
    name = Column(String(55), nullable=False)
    year = Column(Integer, nullable=False)
    dept = Column(String(50), nullable=False)
    login = relationship("Login", backref=backref("students", passive_deletes=True, cascade="all, delete-orphan"))

class Teacher(db.Base):
    __tablename__ = 'teacher'
    staff_id = Column(String(10),ForeignKey('login.username', ondelete='CASCADE'), primary_key=True, nullable=False)
    name = Column(String(55), nullable=False)
    dept = Column(String(50), nullable=False)
    login = relationship("Login", backref=backref("teachers", passive_deletes=True, cascade="all, delete-orphan"))

class Teams(db.Base):
    __tablename__ = 'teams'
    team_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    batch = Column(Integer, nullable=False)
    team_name = Column(String(50), nullable=False)
    team_guide = Column(String(10), ForeignKey('teacher.staff_id', ondelete='CASCADE') , nullable=False)
    guide = relationship("Teacher", backref=backref("teams", passive_deletes=True, cascade="all, delete-orphan"))

class Relation(db.Base):
    __tablename__ ='relation'
    r_id = Column(Integer, primary_key=True, nullable= False, autoincrement=True)
    usn = Column(String(10), ForeignKey('student.usn', ondelete='CASCADE'), nullable=False)
    team = Column(Integer, ForeignKey('teams.team_id', ondelete='CASCADE'),nullable=False)
    student = relationship("Student", backref=backref("relations", passive_deletes=True, cascade="all, delete-orphan"))
    team_ = relationship("Teams", backref=backref("relations", passive_deletes=True, cascade="all, delete-orphan"))

class Marks(db.Base):
    __tablename__ ='marks'
    usn = Column(String(10), ForeignKey('student.usn', ondelete='CASCADE') , primary_key=True, nullable=False)
    report = Column(Integer, nullable=False)
    project = Column(Integer, nullable=False)
    viva = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    student = relationship("Student", backref=backref("marks", passive_deletes=True, cascade="all, delete-orphan"))
