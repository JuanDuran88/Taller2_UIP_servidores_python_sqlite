from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer

engine = create_engine("sqlite:///mydb.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()

# result = [r.username for r in session.query(User).all()]
# from pdb import set_trace; set_trace()

