from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

ProjectYear = Table(
        'ProjectYear', meta,
         Column('Sl ', Integer),
         Column('Year', Integer, primay_key = True), 
         Column('NumberOfProjects', Integer),
         Column('Dep', String(255))
)

ProjectBatch = Table(
        'ProjectBatch', meta,
         Column('ID ', String(255)),
         Column('Year', Integer, ), 
         Column('Section', String(255), primay_key =  True),
         Column('Dep', String(255))
)

Student_detail = Table(
        'Student_detail', meta,
         Column('Sl ', Integer),
         Column('Section', String(255)), 
         Column('USN', String(255), primarykey = True),
         Column('Name', String(255)),
         Column('Batch', Integer),
         Column('TeamName', String(255)),
         Column('Guid', String(255)),
         Column('Dep', String(255))
)

Student_Marks = Table(
        'Student_Marks', meta,
         Column('Sl ', Integer),
         Column('Section', String(255)), 
         Column('USN', String(255), primarykey = True),
         Column('ReportMarks', Integer),
         Column('PresentationMarks', Integer),
         Column('VivaMarks', Integer),
         Column('TotalMarks', Integer),
         Column('Dep', String(255))
)