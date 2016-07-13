import json
with open('target.json','r', encoding='utf-8') as fh:
    data = json.load(fh)

# print(data)

data1 = data['email']
print (data1)