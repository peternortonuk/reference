from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import filedb2, memorydb
from orm_create import User

# create engine
engine = create_engine(filedb2, echo=True)

# create session (the ORM handle to the db)
Session = sessionmaker(bind=engine)
session = Session()

# define inserts
session.add_all([
     User(name='wendy', fullname='Wendy Williams', password='foobar'),
     User(name='mary', fullname='Mary Contrary', password='xxg527'),
     User(name='fred', fullname='Fred Flinstone', password='blah')])

# commit to the db; using a connection from a pool maintained by the engine
session.commit()


