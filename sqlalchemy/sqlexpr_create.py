from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from config import filedb, memorydb


# define the schema
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
engine = create_engine(filedb, echo=True)

# create the schema
metadata.create_all(engine)

