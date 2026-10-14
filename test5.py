class Book:
    def __init__(self,title,author):
     self.title=title
     self.author=author
     self.is_borrowed=False

    def borrow(self):
       self.is_borrowed=True
       print(self.title,"has been borrowed.")

       def return_book(self):
          self.is_borrowed=False
          print(self.title,"has been returned.")

#create a book object
book1=Book("Mens are from Mrs womens are venus","john gray")

#demonstrate borrowing and returning
print(book1.is_borrowed)

book1.borrow()
print(book1.is_borrowed)

book1.return_book()
print(book1.is_borrowed)
