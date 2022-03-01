import xml.etree.ElementTree as ET

tree=ET.parse("book2.xml")

catalog=tree.getroot()

books=catalog.findall("book")

books[0].clear()

tree.write("book5.xml")