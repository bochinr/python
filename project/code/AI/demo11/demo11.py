from data import request_url
import requests
import re
import json

headers = {'Connection':'close'}
url, base_url = request_url.urls()
response = requests.get(url, headers=headers)

pattern = r"JSON.parse\(\'(.*)\'\)\}\,\"7b0b6\""

data = re.search(pattern, response.text)
data_dict = json.loads(data.group(1))
data_dict.keys()