'''
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from config import filedb2, memorydb


# define schema
#   Declarative is a series of extensions that sit on top of the mapper() construct
#   which itself associates the Table object 'users' with the class 'User' eg
#   mapper(User, user)
#   https://docs.sqlalchemy.org/en/latest/orm/mapping_styles.html#classical-mapping

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
engine = create_engine(filedb2, echo=True)

# create schema in the db
# mapper provides access to the same metadata object as before
Base.metadata.create_all(engine)

# show mapping to Table object
print(User.__table__.__repr__())
