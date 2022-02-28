
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

newbook=domtree.createElement("book")
newbook.setAttribute("id","bk113")

author=domtree.createElement("author")
author.appendChild(domtree.createTextNode("pratik K Sarangi"))

title=domtree.createElement("title")
title.appendChild(domtree.createTextNode("python with XML"))

genre=domtree.createElement("genre")
genre.appendChild(domtree.createTextNode("Programmming"))

price=domtree.createElement("price")
price.appendChild(domtree.createTextNode("1000"))

publish_date=domtree.createElement("publish_date")
publish_date.appendChild(domtree.createTextNode("28-02-2021"))

description=domtree.createElement("description")
description.appendChild(domtree.createTextNode("Just Testing the Functionality"))

newbook.appendChild(author)
newbook.appendChild(title)
newbook.appendChild(genre)
newbook.appendChild(price)
newbook.appendChild(publish_date)
newbook.appendChild(description)

category.appendChild(newbook)

with open("book.xml", "w") as f:
    f.write(domtree.toprettyxml())