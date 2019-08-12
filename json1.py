import json

str1 = '{ "name" : "Anil" , "mark": 33 }'

dict =json.loads(str1)

print (dict)
print (dict['name'])
print (dict['mark'])

dict['mark'] = dict['mark'] *2


str2= json.dumps(dict)
print (str2)


