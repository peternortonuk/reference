from pymongo import MongoClient
import json
import os
import pprint as pp

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
query = collection.find({}, {'_id': 0, 'date': 1})
for i in query:
    print i

import pdb; pdb.set_trace()
pass





