from mongoengine import *
from collections import namedtuple

# config settings
connection_details = namedtuple('connection_details', 'host, port, ssl, username, password')

azure = connection_details(
    'cos-mongo.documents.azure.com',
    10255,
    True,
    r'cos-mongo',
    r'GG1Xa8phchZIJDKNo0Y40xiKEeLI60yBZUHJqMQicbmm1Zie980YSc2G63dRSRPtKtdoFVqrnqirV4nXqJfXaQ=='
)

local = connection_details(
    r'mongodb://localhost',
    27017,
    False,
    None,
    None,
)

# select and create connection
selected_connection = azure  # <-- set it here


# define connection
print('host = ', selected_connection.host)
print('port = ', selected_connection.port)
connect(db='tumblelog', host=selected_connection.host,
                        port=selected_connection.port,
                        username=selected_connection.username,
                        password=selected_connection.password,
                        ssl=selected_connection.ssl)


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

