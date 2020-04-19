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
from instructor_made_assignment.model import InstructorMadeAssignment
from notebook.base.handlers import IPythonHandler


from db import bind_engine


# class Instructor(Base):
#     __tablename__ = 'instructor'
#     id = Column(String(128), primary_key=True, default=new_uuid())
#     email = Column(String(128), unique=True, nullable=False)
#     firstname = Column(String(128))
#     lastname = Column(String(128))
#
#     def to_dict(self):
#         """Convert Instructor object to JSON-friendly dict representation"""
#         return {
#             "id":self.id,
#             "username":self.email,
#             "email":self.email,
#             "firstname":self.firstname,
#             "lastname":self.lastname
#         }
#     def __repr__(self):
#         return  '{"id":"%s","email":"%s","firstname":"%s", "lastname":"%s"}'%(self.id, self.email, self.firstname, self.lastname)
#
# ## for student and instructor
# class Course(Base):
#     __tablename__ = 'course'
#     id = Column(String(128), primary_key=True, default=new_uuid())
#     name = Column(String(128), unique=True, nullable=False)
#
#
#     def to_dict(self):
#         """ Convert Course object to JSON-friendly dict representation"""
#         return {
#             "id": self.id,
#             "name": self.name
#         }
#     def __repr__(self):
#         return '{ "id": "%s","name": "%s"}' % (self.id, self.name)
#
#
#






class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # encoded_object = list(obj.timetuple())[0:6]
            # print('time tuple : {}'.format(obj.timetuple()))
            # print('time object : {}'.format(obj))
            # print('time object to str : {}'.format(str(obj)))

            encoded_object = str(obj)

        else:
            encoded_object =json.JSONEncoder.default(self, obj)
        return encoded_object

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


        self.engine = create_engine('mysql+mysqlconnector://root:mysql123@172.17.0.2:3306/nbgrader_db', echo=True)

        # Create session for uploading the class objects to database
        self.db = scoped_session(sessionmaker(autoflush=True, bind=self.engine))
        ### create all the tables if not created
        bind_engine(self.engine)
        # Base.metadata.create_all(bind=self.engine)
        print('%%%%%%%%%%%%%%%%% database connection has started now %%%%%%%%%%%%%%')
    ''' __enter__ and __exit__ allows you to implement objects which can be used easily with the with statement,
        Here, DatabaseConnectionApp object automatically closes the connection once the corresponding 'with' statement goes out of scope'''


    def getDB(self):
        return self

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


    # def find_all_courses_made_by_instructor(self):
    #
    #     instructor_id = self.add_instructor().to_dict().get('id')
    #     query = "select course.name as name, instructor_made_course.courseid as courseid from instructor_made_course join course on course.id = instructor_made_course.courseid where instructor_made_course.instructorid='"+instructor_id+"'"
    #     print('Query is: ',query)
    #     try:
    #         courses = self.db.execute(query)
    #     except Exception:
    #         courses = []
    #         return courses
    #
    #     print('type of courses :: ', type(courses))
    #     print('All courses made by instructor ::')
    #     results = []
    #
    #     # results from sqlalchemy are returned as a list of tuples; this procedure converts it into a list of dicts
    #     for row_number, row in enumerate(courses):
    #         results.append({})
    #         for column_number, value in enumerate(row):
    #             results[row_number][row.keys()[column_number]] = value
    #     print('Results ::', results)
    #     return results
    #
    # def delete_instructor_made_assignment(self, assignmentId):
    #     instructor_made_assignment = []
    #     query = "delete from instructor_made_assignment WHERE instructor_made_assignment.id = '" + assignmentId + "'"
    #     print('Query is: ', query)
    #     try:
    #         instructor_made_assignment = self.db.query(InstructorMadeAssignment).filter(InstructorMadeAssignment.id == assignmentId).first()
    #
    #     except MultipleResultsFound as m:
    #         print('Instructor made assignment id has multiple data : {} with id : {}'.format(m, id))
    #         return instructor_made_assignment
    #     except NoResultFound as n:
    #         print('Instructor made assignment id has no data : {} with id : {}'.format(n, id))
    #         return instructor_made_assignment
    #
    #     try:
    #         if instructor_made_assignment is not None:
    #             print('Instructor made assignment to delete : {}'.format(instructor_made_assignment.to_dict()))
    #             self.db.delete(instructor_made_assignment)
    #             self.db.commit()
    #     except Exception as e:
    #         print('Error while deleting the instructor made assignment with id : {}'.format(assignmentId))
    #         print(e)
    #         self.db.rollback()
    #         instructor_made_assignment = []
    #         return instructor_made_assignment
    #     return instructor_made_assignment


# if __name__ == "__main__":
#     db = CodeHubMySqlConnector()