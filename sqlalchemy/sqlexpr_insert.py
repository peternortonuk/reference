from sqlalchemy import create_engine
from config import filedb, memorydb
from sqlexpr_create import users

# define an insert statement for the users table
ins = users.insert().values(name='jack', fullname='Jack Jones')

# create a connection
engine = create_engine(filedb, echo=True)
conn = engine.connect()

# execute the insert statement
result = conn.execute(ins)

# view the automatically generated id
print(result.inserted_primary_key)
