import requests as rq

import xml.etree.ElementTree as ET

resp= rq.get("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")

root=ET.fromstring(resp.text)
#print (root.tag)

for child in root.findall('./channel/item/title'):
   print (child.text, child.attrib)

