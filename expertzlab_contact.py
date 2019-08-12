import re
import requests

res = requests.get ("http://www.expertzlab.com/contact.php")
print (res.text)

contacts =  re.finditer("\([\d]{2,4}\)[-\s]*[\d]{7,10}", res.text )

for x in contacts:
    print (x)