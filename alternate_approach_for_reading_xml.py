import xml.etree.ElementTree as ET
tree=ET.parse('book.xml')
category=tree.getroot()
# print(category)
#fetching the tag as 
# print(category.tag)

# books=category.findall("book")
books=category.find("book").attrib
print(books)
# print(books)
# count=0
# for book in books:
#     count+=1
#     print(f"Book %d " % count)
#     print(f"Book id is %s " % book.attrib["id"])
    # print(book.find("author").text)
    # print(book.findall("author"))
    # print(type(book.find("author")))
    # print(type(book.findall("author")))
    # print(book.findall("author")[0].text)
    # print(book.findall("title")[0].text)
    # print(book.findall("genre")[0].text)
    # print(book.findall("price")[0].text)
    # print(book.findall("publish_date")[0].text)
    # print(book.findall("description")[0].text)
    # print()
    
    