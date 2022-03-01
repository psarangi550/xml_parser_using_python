import xml.etree.ElementTree as ET
tree=ET.parse("book2.xml")
category=tree.getroot()
# print(category[0].pop("name"))

books=category.findall("book")

# book.pop()
# for book in books: 
#     book.remove(book[0])


tree.write("book3.xml")
