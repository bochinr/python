import json

employee ='{"id":"09", "name":"Nitin", "department":"Finance"}'

new_dict = json.loads(employee)
print(new_dict)
print(type(new_dict))

