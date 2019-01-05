from sqlalchemy import create_engine
from config import filedb1, memorydb
from sqlalchemy import MetaData

# create engine
engine = create_engine(filedb1, echo=True)

# create connection
conn = engine.connect()

# drop the database
metadata = MetaData()
metadata.drop_all(engine)
# this doesnt work!!!!