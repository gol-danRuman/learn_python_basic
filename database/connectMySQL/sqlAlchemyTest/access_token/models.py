'''
    @author Ruman dangol rumancha12@gmail.com
'''
import sqlalchemy
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from db import Base, new_uuid

class AccessToken(Base):
    """Model for user access token"""
    __tablename__ = 'access_token'
    id = Column(String(128), primary_key=True, default=new_uuid())
    email = Column(String(128), unique=True, nullable=False)
    access_token = Column(String(1024), unique=True, nullable=False)
    expires_in = Column(Integer, nullable=False)
    created_date = Column(DateTime(timezone=True), default=func.now())
    modified_date = Column(DateTime(timezone=True), default=func.now())

    def __init__(
            self,
            id: str,
            access_token: str,
            expires_in: int,
            created_date,
            modified_date
    ):
        self.id = id
        self.access_token = access_token
        self.expires_in = expires_in
        self.created_date = created_date
        self.modified_date = modified_date

    def to_dict(self):
        """ Convert AccessToken object to JSON-friendly dict representation"""
        return {
            "id": self.id,
            "access_token": self.access_token,
            "expires_in": self.expires_in,
            "created_date": self.created_date,
            "modified_date": self.modified_date
        }

    def __repr__(self):
        return "<AccessToken(id='%s, access_token='%s', expires_in='%s', created_date='%s', modified_date='%s')>" % (
            self.id,
            self.access_token,
            self.expires_in,
            self.created_date,
            self.modified_date
        )
