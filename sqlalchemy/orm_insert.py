from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import filedb, memorydb
from orm_create import User

# create engine
engine = create_engine(filedb, echo=True)

# create a session
Session = sessionmaker(bind=engine)
session = Session()

# insert rows of data
session.add_all([
     User(name='wendy', fullname='Wendy Williams', password='foobar'),
     User(name='mary', fullname='Mary Contrary', password='xxg527'),
     User(name='fred', fullname='Fred Flinstone', password='blah')])
session.commit()


