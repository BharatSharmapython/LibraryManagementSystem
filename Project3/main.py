class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailibleBooks(self):
        print("Books availible in this library are: ")
        for book in self.books:
            print(" *"+book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it in 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry this book is either not availible or has already been issued to someone else. Please wait until the book is availible")    
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning this Book! Hope you enjoyed reading it. Have a great day ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
        

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django","Clrs","ProgrammingwithC","PythonNotes"])
    student = Student()
    while(True):
        welcomemsg ='''
        ======Welcome To Central Library=====
        Please choose an option:
        1. Listing all books
        2. Request a Book
        3. Add/Return a Book
        4. Exit the Library
        '''
        print(welcomemsg)
        a = int(input("Enter a choice"))
        if a == 1:
            centralLibrary.displayAvailibleBooks()

        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thanks for using choosing Central Library! Have a great day ahead!")
            exit()

        else:
            print("Invalid Choice!")