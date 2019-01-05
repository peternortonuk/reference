from sqlalchemy import create_engine
from config import filedb1, memorydb
from sqlexpr_create import users

# create engine
engine = create_engine(filedb1, echo=True)

# create connection
conn = engine.connect()

# define inserts
ins = users.insert().values(name='jack', fullname='Jack Jones')

# execute on the db
result = conn.execute(ins)

# view the automatically generated id
print(result.inserted_primary_key)
