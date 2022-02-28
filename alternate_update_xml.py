import xml.etree.ElementTree as ET

def update_xml(filename):
    tree=ET.ElementTree(file=filename)
    category=tree.getroot()
    for price in iter(category.findall("price")):
        price.text="110"
        print(dir(price))
    
    tree=ET.ElementTree(category)
    
    with open(filename,"wb") as f:
        tree.write(f)

if __name__=="__main__":
    update_xml("book.xml")