import xml.etree.ElementTree as ET

tree=ET.parse("book2.xml")

category=tree.getroot()

print(category[0].attrib["id"])

# books=category.findall("book")

# prices=ET.SubElement(book, "price")
# price.text="100"

# for book in books: 
#     price=ET.SubElement(book, "price")
#     price.text="100"
#     # print(price.text)

# tree.write("book2.xml")