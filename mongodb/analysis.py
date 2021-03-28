from pymongo import MongoClient
import json
import os

# location of json file
rel_path = r'data'
file = r'crimes_street_dates.json'
pathfile = os.path.join(os.path.dirname(__file__), rel_path, file)

# load into variable
with open(pathfile) as json_data:
    data = json.load(json_data)

# start the client
client = MongoClient()

# create a new database and collection
db = client.crime_database
collection = db.crime_database

# bulk insert json data from file
result = collection.insert_many(data)

# analysis
print('========================')
results = collection.find({},                     # where this is true
                          {'_id': 0, 'date': 1},  # select these fields
                          )
for i in results:
    print(i)
print('========================')

print('========================')
results = collection.find(
    {'$and': [{'date': '2018-01'},
              {'stop-and-search': {'$exists': 'true', '$in': ['btp']}},
              ]}
)
for i in results:
    print(i)
print('========================')

client.drop_database(db)
pass

