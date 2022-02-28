import xml.etree.ElementTree as ET

# root=ET.Element("category")

# book=ET.Element("book")

# root.append(book)

# book.attrib["id"]="11"

# name=ET.SubElement(book, "name")
# name.text="python"
# name.attrib["value"]="1"

# tree=ET.ElementTree(root)

###updating the existing info ####

tree=ET.ElementTree(file="book2.xml")

category=tree.getroot()

books=category.findall("book")

# print(books)

print(books[0].find("name").text)

# for name in category.iter("name"):
#     name.text="flask"

for book in books:
    for name in book.findall("name"):
        name.text="django"

tree=ET.ElementTree(category)

with open("book2.xml","wb") as f:
    tree.write(f)