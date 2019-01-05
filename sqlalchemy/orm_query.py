from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import filedb, memorydb
from orm_create import User

# create engine
engine = create_engine(filedb, echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# query the data
our_user = session.query(User).filter_by(name='fred').all()
print(our_user)
