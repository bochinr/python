import json

with open("record.json",'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
    print(type(load_dict))
