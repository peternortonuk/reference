from sqlalchemy import create_engine
from sqlalchemy.sql import select, text
from config import filedb1, memorydb
from sqlexpr_create import users

# create engine
engine = create_engine(filedb1, echo=True)

# create connection
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
