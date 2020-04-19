from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from uuid import uuid4

Base = declarative_base()
Session = sessionmaker()

def bind_engine(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(bind=engine)
    Session.configure(bind=engine)



def new_uuid():
    id_value = uuid4().hex
    # print('################################################################')
    # print(id_value)
    return id_value

class MissingEntry(ValueError):
    pass