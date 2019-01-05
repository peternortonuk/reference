from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.sql import select
from config import filedb, memorydb
from sqlexpr_create import users

# create connection
engine = create_engine(filedb, echo=True)
conn = engine.connect()

# select from the table
s = select([users])  # sql expression language
results = conn.execute(s)
for record in results:
    print(record)
results.close()
print('===')

s = text("SELECT * FROM users")  # sql text
results = conn.execute(s)
for record in results:
    print(record)
results.close()
print('===')
