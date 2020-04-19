import json
import os
import requests
import datetime
from uuid import uuid4
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean,VARCHAR,TEXT,NVARCHAR, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, Query
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import DatabaseError

from notebook.base.handlers import IPythonHandler
# from dbHandler import Base
# Base = declarative_base()
from db import Base, new_uuid


class InstructorMadeAssignment(Base):
    __tablename__ = 'instructor_made_assignment'
    id = Column(String(128), primary_key=True, default=new_uuid())
    name = Column(String(128),unique=True, nullable=False)
    # courseid = Column(String(128), ForeignKey('course.id'))
    # instructorid = Column(String(128), ForeignKey('instructor.id'))
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    notebook_url = Column(String(128), nullable=False)
    def to_dict(self):
        """ Convert Assignment object to JSON-friendly dict representation"""
        return {
            "id": self.id,
            "name": self.name,
            # "courseid": self.courseid,
            # "instructorid":self.instructorid,
            "created_time": self.created_time,
            "notebook_url": self.notebook_url
        }
    def __repr__(self):
        return "<InstructorMadeAssignment(id='%s',name='%s', created_time='%s', notebook_url='%s)>" % (self.id,self.name, self.created_time, self.notebook_url)
    #     return '{ "Id": "{}","name": "{}", "created_time": "{:%Y-%m-%d %H:%M}", "notebook_url": "{}"}'.format(self.id, self.name, self.created_time, self.notebook_url)
