import xml.dom.minidom

domtree=xml.dom.minidom.parse("book2.xml")

new_category=domtree.documentElement

book=domtree.createElement("book")
book.setAttribute("id","13")
new_category.appendChild(book)

name=domtree.createElement("name")
name.appendChild(domtree.createTextNode("kubernetes"))
book.appendChild(name)
domtree.appendChild(new_category)

domtree.writexml(open("book2.xml","w"))



