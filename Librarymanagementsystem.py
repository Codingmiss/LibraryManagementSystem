class Library:
    def __init__(self):
        self.file = open('books.txt', 'a+')

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        print(lines)
        self.file.close() 

        
        for line in lines:
            book_info = line.split()
            print(f'Book: {book_info[0]}')
            print(f'Author: {book_info[1]}')
            print()

    def add_book(self, title, author, releaseYear, numberofPages):
        bookInfos = (f"{title}, {author}, {releaseYear}, {numberofPages}\n")
        self.file.write(bookInfos)
        self.file.close() 

    def remove_book(self, title):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        self.file.close() 

        books = []
        indexforDelete = -1
        for i, line in enumerate(lines):
            if title in line:
                indexforDelete = i
                break

        if indexforDelete != -1:
            del lines[indexforDelete]

        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            self.file.write(line + '\n')

    def menu(self):
        while True:
            print("***** MENU*****")
            print("1. List Books")
            print("2. Add Book")
            print("3. Remove Book")
            print("4. Quit")
            
            menu_choice = input("Enter your choice (1-4): ")
            
            if menu_choice == "1":
                self.list_books()
            elif menu_choice == "2":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                releaseYear = input("Enter release year: ")
                numberofPages = input("Enter number of pages: ")
                self.add_book(title, author, releaseYear, numberofPages)
            elif menu_choice == "3":
                title = input("Enter the title of the book to remove: ")
                self.remove_book(title)
            elif menu_choice == "4":
                break
            else:
                print("Wrong choice. Please enter a number between 1 and 4.")

lib = Library()
lib.menu()
