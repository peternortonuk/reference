import pymongo
import getpass
import os


cert_file_path = r'c:\temp\GMT-RootCA.PEM'
assert os.path.isfile(cert_file_path), 'SSL Certificate not found: %s' % cert_file_path

c = pymongo.MongoClient(
      host=r'GMPR-MGOSVR01.GAZPROMUK.INTRA,GMPR-MGOSVR02.GAZPROMUK.INTRA,GMPR-MGOSVR03.GAZPROMUK.INTRA',
      port=27017,
      replicaSet='gmpr-mgorep01',
      # readPreference='primary', # primary is already default
      ssl=True,
      ssl_ca_certs=cert_file_path,
      username='%s@GAZPROMUK.INTRA' % raw_input('Username: '),
      password=getpass.getpass('Password: '),
      authMechanism='PLAIN',
      )


cursor = c.list_databases()

for row in cursor:
      print row
