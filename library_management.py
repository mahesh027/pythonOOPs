#abstraction and encapsulation in python// eg.library management
class library:
    def __init__(self,books):
        self.book=books
    def list_book(self):
        print("available books:")
        for x in self.book:
            print(x)
    def borrow_book(self,borrow_book):
        if borrow_book in self.book:
            print("get your book now")
            self.book.remove(borrow_book)
        else:
            print("book not available")
    def receive_book(self,receive_book):
        print("you have returned the book")
        self.book.append(receive_book)
books=['c','c++','java','python','flutter','machinelearnning']
o=library(books)
msg= """"
     1.Display books
     2.borrow books
     3.return book
"""
while True:
    print(msg)
    ch=int(input("enter your choice:"))
    if ch==1:
        o.list_book()
    elif ch==2:
        x=input("enter the book to borrow")
        o.borrow_book(x)
    elif ch==3:
        y=input("enter the book returned:")
        o.receive_book(y)
    else:
        print("thank you com again")
        quit()