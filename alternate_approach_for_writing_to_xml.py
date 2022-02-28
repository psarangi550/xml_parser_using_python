import xml.etree.ElementTree as ET

def create_xml_element(filename):
    root=ET.Element("catalog")
    # book=ET.Element("book")
    # book.attrib["id"]="10"
    # root.append(book)
    while True:
        book_id=input("Enter the book ID")
        author_input=input("Enter the Author Name")
        title_input=input("Enter the Tittle Of the Book")
        genre_input=input("Enter the Genre of the BOok")
        price_input=input("Enter the Price for the book")
        publish_date_input=input("Enter the Published_Date for the book")
        description_input=input("Enter the Description for the book")
        book=ET.Element("book")
        root.append(book)
        book.attrib["id"]=book_id
        author=ET.SubElement(book, "author")
        author.text = author_input
        title=ET.SubElement(book, "title")
        title.text = title_input
        genre=ET.SubElement(book, "genre")
        genre.text = genre_input
        price=ET.SubElement(book, "price")
        price.text = price_input
        publish_date=ET.SubElement(book, "publish_date")
        publish_date.text = publish_date_input
        description=ET.SubElement(book, "description")
        description.text = description_input
        tree=ET.ElementTree(root) 
        option=input("do you want to Add one More Book [y/n]")
        if option.lower() == "n":
            break
    
    with open(filename,"wb") as f:
        tree.write(f)

if __name__ == "__main__":
    create_xml_element("book1.xml")
        
        
        
        
        
        
        
        
    
    
    