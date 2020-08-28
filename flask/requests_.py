import requests
from pprint import pprint as pp

url = r'http://localhost:5000/api/people'
resp = requests.get(url=url)
json = resp.json()
pp(json)
