import xml.etree.ElementTree as ET

tree=ET.parse("book2.xml")

category=tree.getroot()

books=category.findall("book")

for book in books:
    print(book.attrib.pop("id"))
    
tree.write("book4.xml")
