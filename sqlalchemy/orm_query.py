from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import filedb2, memorydb
from orm_create import User

# create engine
engine = create_engine(filedb2, echo=True)

# create session (the ORM handle to the db)
Session = sessionmaker(bind=engine)
session = Session()

# query the data; using a connection from a pool maintained by the engine
our_user = session.query(User).filter_by(name='fred').all()
print(our_user)
