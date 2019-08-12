import requests as rq
import json

res= rq.get ("https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=26084459")

#res = rq.get("http://www.expertzlab.com")
#print (res.text)
mydata = json.loads(res.text)
#print (mydata)

for k,v in mydata['navData'].items():
   print (k , "---" , v ['title'], )
   print ("----------")
