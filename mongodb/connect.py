from pymongo import MongoClient
import datetime
import pprint as pp

# some test data; a pretend blog post
post = {'author': 'Mike',
        'text': 'My first blog post!',
        'tags': ['mongodb', 'python', 'pymongo'],
        'date': datetime.datetime.utcnow()}

contact = {'name': 'Pete',
        'phone': '07884 123123',
        'address': ['my house, 123 the street'],}

mixup = {'author': 'Mike',
        'phone': '07884 123123',
        'address': ['my house, 123 the street'],}

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
print(id)

# find_one() <--
# find the first document returned from the collection
doc = collection.find_one()
print(doc)

# now insert the contact and the other one
result = collection.insert_one(contact)
result = collection.insert_one(mixup)

# find_one() <--
# find the first document returned from the collection that matches
print(collection.find_one({'text': 'My first blog post!'}))
print(collection.find_one({'phone': '07884 123123'}))

# find() <--
# find all documents matching this search and return a 'pymongo.cursor.Cursor'
# then iterate over the results
results = collection.find({'author': 'Mike'})
for item in results:
        print(item)

# cursor has count method
print(results.count())

# find() <--
# range queries and sort
# https://docs.mongodb.com/manual/reference/operator/query/
d = datetime.datetime(2009, 11, 12, 12)
results = collection.find({"date": {"$gt": d}}).sort("author")
for item in results:
        print(item)

# drop the database
import pdb; pdb.set_trace()
client.drop_database(db)