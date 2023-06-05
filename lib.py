lib=[]
borrow=[]
class Library:
    def add_book(self):
        self.title=input("enter the title of book=")
        self.author=input("enter the author of book=")
        self.copies=int(input("enter the number of copies of book="))
    def search_book(self):
        if len(lib)!=0:
            self.count=0
            self.searc_book=input("enter the title of book to searcg=")
            for i in lib:
                if i.title==self.searc_book:
                    print(f"{i.title} is available and have {i.copies} copies")
                    break
                print("book not available")
                break
            print("currently none books are present")
    def display_book(self):
        print("List of books=")
        for i in lib:
            print(i.title)
    def display_available_book(self):
        print("List of available books=")
        if len(lib)!=0:
            for i in lib:
                if i.copies!=0:
                    print(i.title," ",i.copies)
        else:        
            print("currently none books are available")

    def display_borrowed_books(self):
        print("List of borrowers:")
        if len(borrow)!=0:
            for i in borrow:
                print(f"{i.borrower_name}  {i.borrower_title} {i.author}")
        else:
            print("no borrowers")
    def borrow_book(self):
        self.borrower_name=input("enter your name=")
        self.borrower_title=input("enter the title of the book=")
        for i in lib:
            if i.title == self.borrower_title:
                if i.copies==0:
                    print("Book is not available to borrow")
                    break
                i.copies-=1
                self.author=i.author
                break
            
            print("Book is not found")
    def return_book(self):
        self.name=input("enter the name=")
        self.title=input("enter the titlt=")
        for i in borrow:
            if i.borrower_name==self.name and i.borrower_title==self.title:
                borrow.remove(i)
        for i in lib:
            if self.title==i.title:
                i.copies+=1
                print("book returned")
                break
while True:
    print("1. do you wanna add book")
    print("2.do you wanna search book")
    print("3. list of books")
    print("4. available book")
    print("5. display borrowed books")
    print("6. do you wanna borrow")
    print("7. do you wanna return")
    print("8. quit")
    choice=input("enter your choice=")
    if choice=="1":
        newO=Library()
        newO.add_book()
        lib.append(newO)
    elif choice=="2":
        newO=Library()
        newO.search_book()
    elif choice=="3":
        newO=Library()
        newO.display_book()
    elif choice=="4":
        newO=Library()
        newO.display_available_book()
    elif choice=="5":
        newO=Library()
        newO.display_borrowed_books()
        
    elif choice=="6":
        newO=Library()
        newO.borrow_book()
        borrow.append(newO)
    elif choice=="7":
        newO=Library()
        newO.return_book()
    elif choice=="8":
        break
    else:
        print("invalid choice")