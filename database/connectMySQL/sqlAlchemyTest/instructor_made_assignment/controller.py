
from sqlalchemy.orm.exc import NoResultFound
from .model import InstructorMadeAssignment
from db import Session

class InstructorMadeAssignmentController:
    @classmethod
    def find_all(self):
        try:
            session = Session()
            print(session.query(InstructorMadeAssignment).filter(InstructorMadeAssignment.id == "1").all())
        except NoResultFound:
            list_of_assignments = []
        # return list_of_assignments
