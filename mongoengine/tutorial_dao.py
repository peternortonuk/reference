from mongoengine import *


host = r'cos-mongo.documents.azure.com'
port = 10255
username = r'cos-mongo'
password = r'GG1Xa8phchZIJDKNo0Y40xiKEeLI60yBZUHJqMQicbmm1Zie980YSc2G63dRSRPtKtdoFVqrnqirV4nXqJfXaQ=='
connection_string = r'mongodb://cos-mongo:GG1Xa8phchZIJDKNo0Y40xiKEeLI60yBZUHJqMQicbmm1Zie980YSc2G63dRSRPtKtdoFVqrnqirV4nXqJfXaQ==@cos-mongo.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'

connect(db='tumblelog', host=host, port=port, username=username, password=password)

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()

