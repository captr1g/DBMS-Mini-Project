from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Database_URL = "mysql+pymysql://alumni_root:12345678@db4free.net:3306/alumni"
engine = create_engine(Database_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()