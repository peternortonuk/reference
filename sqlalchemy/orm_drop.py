from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import filedb2, memorydb
from sqlalchemy.ext.declarative import declarative_base

# create engine
engine = create_engine(filedb2, echo=True)

# create session (the ORM handle to the db)
Session = sessionmaker(bind=engine)
session = Session()

# drop the database
Base = declarative_base()
Base.metadata.drop_all(engine)
# this doesnt work!!!!
