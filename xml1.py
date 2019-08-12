import xml.etree.ElementTree as abc

data = abc.parse("data.xml")
root = data.getroot()

print (root.tag)

for x in root:
   print (x.tag, x.attrib)
   for y in x:
       print("    ", y.tag, y.attrib, y.text)

