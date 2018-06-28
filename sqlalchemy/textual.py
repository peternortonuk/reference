from sqlalchemy import create_engine
from sqlalchemy.sql import text


engine = create_engine('sqlite:///:memory:', echo=True)
conn = engine.connect()

s = text("SELECT * FROM users")  # sql text
results = conn.execute(s)
for record in results:
    print(record)
results.close()
print('===')




