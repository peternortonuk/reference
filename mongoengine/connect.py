import pymongo
import getpass
import os

connect_dict = {
      'prod': {
            'host': r'GMPR-MGOSVR01.GAZPROMUK.INTRA,GMPR-MGOSVR02.GAZPROMUK.INTRA,GMPR-MGOSVR03.GAZPROMUK.INTRA',
            'replicaset': r'gmpr-mgorep01',
            'username': r'svc-gmt-pr-mgo-orc',
            'password': r'ycH5RED?yTya^QX!mG87$',
      },
      'dev': {
            'host': r'GMDV-MGOSVR01.gazpromuk.intra,GMDV-MGOSVR02.gazpromuk.intra,GMDV-MGOSVR03.gazpromuk.intra',
            'replicaset': r'gmdv-mgorep01',
            'username': r'svc-gmt-dv-mgo-orc',
            'password': r'RED?cH5$a^QyTX!mG8y7$',
      }
}

cert_file_path = r'c:\temp\GMT-RootCA.PEM'
assert os.path.isfile(cert_file_path), 'SSL Certificate not found: %s' % cert_file_path


def create_connection_and_list_dbs(host, replicaset, username, password):
      c = pymongo.MongoClient(
            host=host,
            port=27017,
            replicaSet=replicaset,
            # readPreference='primary', # primary is already default
            ssl=True,
            ssl_ca_certs=cert_file_path,
            username='%s@GAZPROMUK.INTRA' % username,
            password=password,
            authMechanism='PLAIN',
            )

      cursor = c.list_databases()

      for row in cursor:
            print row


host_key = raw_input('Environment: ')
svc_user_key = raw_input('User [prod, dev or username]: ')

host = connect_dict[host_key]['host']
replicaset = connect_dict[host_key]['replicaset']

if svc_user_key in connect_dict.keys():
      username = connect_dict[host_key]['username']
      password = connect_dict[host_key]['password']
else:
      username = svc_user_key
      password = getpass.getpass('Password: ')


create_connection_and_list_dbs(host, replicaset, username, password)