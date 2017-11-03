#!c::\dev\bin\anaconda\python
# -*- coding: utf-8 -*-

'''
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


# The return value of create_engine() is an instance of Engine,
# and it represents the core interface to the database, adapted
# through a dialect that handles the details of the database and DBAPI in use.
# In this case the SQLite dialect will interpret instructions to the Python built-in sqlite3 module.


# When using the ORM, we typically dont use the Engine directly once created;
# instead, its used behind the scenes by the ORM
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % \
            (self.name, self.fullname, self.password)

# create engine
engine = create_engine('sqlite:///:memory:', echo=True)

# create the db objects
Base.metadata.create_all(engine)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# insert rows of data
session.add_all([
     User(name='wendy', fullname='Wendy Williams', password='foobar'),
     User(name='mary', fullname='Mary Contrary', password='xxg527'),
     User(name='fred', fullname='Fred Flinstone', password='blah')])
session.commit()

# query the data
our_user = session.query(User).filter_by(name='fred').all()
print our_user
