from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

ProjectYear = Table(
        'ProjectYear', meta,
         Column('U_Year', Integer),
         Column('Year', Integer, primay_key = True), 
         Column('NumberOfProjects', Integer),
         Column('Dep', String(255))
)

ProjectBatch = Table(
        'ProjectBatch', meta,
         Column('U_Sec', String(255)),
         Column('Year', String), #U_Year
         Column('Section', String(255)),
)

Team = Table(
        'Teams', meta,
        Column('Team ID'),
        Column('Team Name'),
        Column('Team Guide'),
        Column('Batch_Year'), #U_Year
)

Student_detail = Table(
        'Student_detail', meta,
         Column('USN', String(255), primarykey = True),
         Column('Name', String(255)),
        #  extra info of student
         Column('class', String),#U_Sec
)

Student_team = Table(
        'Teams_detail', meta,
        Column('Team ID'),
        Column('USN') ##
)

Student_Marks = Table(
        'Student_Marks', meta,
         Column('class', String),#U_Sec
         Column('USN', String(255), primarykey = True),
         Column('ReportMarks', Integer),
         Column('PresentationMarks', Integer),
         Column('VivaMarks', Integer),
         Column('TotalMarks', Integer),
)