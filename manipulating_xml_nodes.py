import xml.dom.minidom

domtree=xml.dom.minidom.parse('book.xml')
category=domtree.documentElement
books=category.getElementsByTagName('book')
count=0
for book in books:
    count=count+1
    print(f"BOOK %d " %count)
    print("--------------------------------")
    if book.hasAttribute('id'):
        print(book.getAttribute('id'))
    author=book.getElementsByTagName('author')[0].childNodes[0].nodeValue
    title=book.getElementsByTagName('title')[0].childNodes[0].nodeValue
    genre=book.getElementsByTagName('genre')[0].childNodes[0].nodeValue
    price=book.getElementsByTagName('price')[0].childNodes[0].nodeValue
    publish_date=book.getElementsByTagName('publish_date')[0].childNodes[0].nodeValue
    description=book.getElementsByTagName('description')[0].childNodes[0].nodeValue
    
    print(f"author: {author}")
    print(f"title: {title}")
    print(f"genre: {genre}")
    print(f"price: {price}")
    print(f"publish_date: {publish_date}")
    print(f"description: {description}")

#manipulatingXmlNodes
books[0].getElementsByTagName('author')[0].childNodes[0].nodeValue ="Abismruta Sarangi"
books[0].setAttribute('id','100')

domtree.writexml(open('book.xml','w'))
    
    

