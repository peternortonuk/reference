from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from sqlalchemy.sql import text


# a repository for data connections; here using in-memory db
engine = create_engine('sqlite:///:memory:', echo=True)

# define the schema
metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

# create the schema
metadata.create_all(engine)

# define an insert statement for the users table
ins = users.insert().values(name='jack', fullname='Jack Jones')

# create a connection and execute the insert statement
conn = engine.connect()
result = conn.execute(ins)

# view the automatically generated id
print(result.inserted_primary_key)

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