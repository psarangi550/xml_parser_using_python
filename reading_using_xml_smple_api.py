import xml.sax

class BookHandler(xml.sax.ContentHandler):
    
    def startElement(self, name, attrs):
        self.current=name
        if self.current=="book":
            print(f"----BOOK {attrs['id']}----")
            print(f"ID of the Book is {attrs['id']}")
    
    def characters(self,content):
        if self.current=="author":
            self.author=content
        if self.current=="title":
            self.title=content
        if self.current=="genre":
            self.genre=content
        if self.current=="price":
            self.price=content
        if self.current=="publish_date":
            self.publish_date=content
        if self.current=="description":
            self.description=content
    
    def endElement(self,name):
        if self.current=="author":
            print(self.author)
        if self.current=="title":
            print(self.title)
        if self.current=="genre":
            print(self.genre)
        if self.current=="price":
            print(self.price)
        if self.current=="publish_date":
            print(self.publish_date)
        if self.current=="description":
            print(self.description)
        self.current=""
                

handler=BookHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('book.xml')
            