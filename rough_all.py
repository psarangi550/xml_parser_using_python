import xml.etree.ElementTree as ET

tree=ET.parse("book2.xml")

root=tree.getroot()

# tree=ET.fromstring('''
#     <catalog>
#     <book id="11">
#         <author>rika</author>
#         <title>python</title>
#         <genre>prog</genre>
#         <price>10</price>
#         <publish_date>12-02-2022</publish_date>
#         <description>programing</description>
#     </book>
#     </catalog>               
#     ''')
# print(tree)
# print(type(tree))
# print(tree.getroot().findall("book"))

for book in root.findall("book"):
    book.remove(book.find("name"))

tree.write("book6.xml")