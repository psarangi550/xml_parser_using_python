import xml.dom.minidom

books_data =xml.dom.minidom.parse('book.xml')

catalog=books_data.documentElement

books=catalog.getElementsByTagName("book")

for book in books:
    print(f'Book Attribute---->{book.getAttribute("id")}')
    print(f'Book Author---->{len(book.childNodes)}')
    # print(f'Book Author---->{book.childNodes[9].childNodes[0][0]}')
    # print(f'Book Author---->{indexof(book.childNodes,"publish_date")}')
    print(f'Book Author---->{book.childNodes[1].childNodes[0].nodeValue}')
    print(f'Book title---->{book.childNodes[3].childNodes[0].nodeValue}')
    print(f'Book genre---->{book.childNodes[5].childNodes[0].nodeValue}')
    print(f'Book price---->{book.childNodes[7].childNodes[0].nodeValue}')
    print(f'Book description---->{book.childNodes[11].childNodes[0].nodeValue}')
    
    #alternate Approaches:-
    
    # print(f"Book Child Element 1 is {book.childNodes[0].nodeValue}")
    # author=book.getElementsByTagName('author')[0].childNodes[0].nodeValue
    # title=book.getElementsByTagName('title')[0].childNodes[0].nodeValue
    # genre=book.getElementsByTagName('genre')[0].childNodes[0].nodeValue
    # publish_date=book.getElementsByTagName('publish_date')[0].childNodes[0].nodeValue
    # description=book.getElementsByTagName('description')[0].childNodes[0].nodeValue
    # print(f'Author Name:---->{author}')
    # print(f'Title Name:---->{title}')
    # print(f'Genre:---->{genre}')
    # print(f'Publish Date:---->{publish_date}')
    # print(f'Description:---->{description}')
    print()
    # print(type(author))
    # print(dir(author))
    # break 
    


