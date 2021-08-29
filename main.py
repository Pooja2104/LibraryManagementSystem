class Library:

    def __init__(self,ListOfBooks):
        self.Books = ListOfBooks

    def DisplayAvailableBooks(self):
        print("Books Present in library:")
        for Book in self.Books:
            print("\t" + Book)

    def BorrowBook(self,BookName):
        if BookName in self.Books:
            print(f"You have been issued {BookName}. Please handle it with care and return within 30 days.")
            self.Books.remove(BookName)
            return True
        else:
            print("Sorry, This book is not available or issued by someone else.Please wait until the book is available.")
            return False

    def returnBook(self,BookName):
        self.Books.append(BookName)
        print("Thanks for returning this Book!!")




class Student:
    def requestBook(self):
        self.Book = input("Enter the book name you want to borrow:")
        return self.Book

    def returnBook(self):
        self.Book = input("Enter the book name you want to return:")
        return self.Book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithm","Django","MongoDB","Python","SQL"])
    student = Student()
    #centralLibrary.DisplayAvailableBooks()

    while(True):
        WelcomeMSG = '''\n Welcome to Central Library
        Please Choose one option:
        1.List of all the books
        2.Request a book
        3.Return a book
        4.Exit
        '''
        print(WelcomeMSG)
        input = int(input("Enter a choice:"))
        if input == 1:
            print(centralLibrary.DisplayAvailableBooks())
        elif input == 2:
            print(centralLibrary.BorrowBook(student.requestBook()))
        elif input == 3:
            print(centralLibrary.returnBook(student.requestBook()))
        elif input == 4:
            print("Thanks!!")
            exit()
        else:
            print("Invalid Choice")









