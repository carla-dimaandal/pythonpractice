class Book(object):
    def get_book(self):
        print("To Kill a Mocking Bird")


class Author(Book):
    def get_author(self):
        print("Harper Lee")

bk = Book()
bk.get_book() 
print("--------")

au = Author()
au.get_author()  
au.get_book()
