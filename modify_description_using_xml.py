import xml.etree.ElementTree as ET

tree=ET.parse("book.xml")

catalog=tree.getroot()

# print(catalog)

for desc in catalog.iter("description"):
    desc.text = desc.text+"Hello"
    desc.set("updated","yes")
tree=ET.ElementTree(catalog)

with open("book.xml","wb") as f: 
    tree.write(f)     


