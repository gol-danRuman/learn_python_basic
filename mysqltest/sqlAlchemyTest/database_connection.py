
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

Base = declarative_base()

class CodeHubMySqlConnector:
    def __init__(self):
        print('^^^^^^^^^^^ database connection is about to start ^^^^^^^^^^^^^')
        print('SqlAlchemy Version: ', sqlalchemy.__version__)
        # db_url = DB_URL
        ##Create sqlalchemy engine
        # environment = os.getenv('ENVIRONMENT')
        # if environment == 'production':
        #     db_url = 'mysql+mysqlconnector://root:test123@10.48.128.3:3306/nbgrader_db'
        # elif environment == 'stage':
        #     db_url = 'mysql+mysqlconnector://root:test123@10.48.128.3:3306/nbgrader_db'
        # else:
        #     # db_url = 'mysql+mysqlconnector://root:test123@10.48.128.3:3306/nbgrader_db'  ## for development
        #     ##db_url = 'mysql+mysqlconnector://root:mysql123@172.20.0.2:3306/nbgrader_db' ## for local Manshi
        #     db_url = 'mysql+mysqlconnector://root:mysql123@172.18.0.2:3306/nbgrader_db'  ## for local Ruman

        # print('Our environment is {}'.format(environment))


        self.engine = create_engine('mysql+mysqlconnector://root:mysql123@172.18.0.2:3306/nbgrader_db', echo=True)
        # Create session for uploading the class objects to database
        self.db = scoped_session(sessionmaker(autoflush=True, bind=self.engine))
        ### create all the tables if not created
        Base.metadata.create_all(bind=self.engine)
        print('%%%%%%%%%%%%%%%%% database connection has started now %%%%%%%%%%%%%%')
    ''' __enter__ and __exit__ allows you to implement objects which can be used easily with the with statement,
        Here, DatabaseConnectionApp object automatically closes the connection once the corresponding 'with' statement goes out of scope'''

    # make databse connection and return it
    def __enter__(self):
        return self

    # make sure the dbconnection gets closed
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """Close the connection to the database.

        It is important to call this method after you are done using the
        DatabaseConnectionApp. In particular, if you create multiple instances of the
        DatabaseConnectionApp without closing them, you may run into errors where there
        are too many open connections to the database.

        """
        self.db.remove()
        self.engine.dispose()