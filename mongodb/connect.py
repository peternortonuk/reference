from pymongo import MongoClient
import datetime
import pprint as pp

# some test data; a pretend blog post
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

contact = {"name": "Pete",
        "phone": "07884 123123",
        "address": ["my house, 123 the street"],}

import pdb; pdb.set_trace()

# start the client
client = MongoClient()

# create a new database; called test_database
db = client.test_database

# create a collection; called test_collection
# a collection is a group of documents, roughly equivalent to a table
collection = db.test_collection

# insert blog post as a document
# the returned object is the result of the insert
result = collection.insert_one(post)

# the result object has a record of the automatically inserted id
id = result.inserted_id

# show the object id
print id

# print the first document returned from the collection
doc = collection.find_one()
print doc

# now insert the contact
result = collection.insert_one(contact)

# query the collection
print collection.find_one({'text': 'My first blog post!'})
print collection.find_one({'phone': '07884 123123'})


# drop the database
import pdb; pdb.set_trace()
client.drop_database(db)