'''
https://docs.sqlalchemy.org/en/latest/core/tutorial.html
'''

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from config import filedb1, memorydb


# define schema
#   MetaData defines the collection of Table objects
#   and associated child Column objects

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

# create engine
engine = create_engine(filedb1, echo=True)

# create schema in the db
metadata.create_all(engine)

