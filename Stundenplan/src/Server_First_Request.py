import json

import httplib2
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

queue = list()

http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
url = 'http://localhost:35786/solver/'
headers = {'Content-type':'application/json','Accept':'application/json','Authorization':'Token token="abc"'}
resp, content = http.request(url, 'GET', headers=headers)
print(resp)
print(content)