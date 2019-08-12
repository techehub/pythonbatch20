import json

str1 = '{ "name" : "Anil" , "mark": 33 }'
dict =json.loads(str1)

dict['mark'] = dict['mark'] *2

str2= json.dumps(dict)
print (str2)

########

with open ("data.json") as fp:
   #str1 = fp.read()
   dict =json.load(fp)

dict['mark'] = dict['mark'] *2

with open ("data1.json","w") as fp:
    json.dump(dict,fp)


