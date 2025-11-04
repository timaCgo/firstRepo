class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    def __str__(self):
        status = "Взята" if self.is_borrowed else "Доступна"
        return f"Название книги: {self.title}, автор: {self.author}, статус: {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:  
                if not book.is_borrowed:  
                    book.is_borrowed = True
                    return f"Можете взять книгу '{title}'"
                else:
                    return "Книга уже взята"
        return "Такой книги нет"

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False  
                    return "Вы вернули книгу"
                else:
                    return "Ошибка: книга не была взята"
        return "Такой книги нет"
    
    def search_author(self, author):
        res = [book for book in self.books if Book.author == author]
        if res:
            return f"{res}"
        else:
            return f"Такой книги нету"
        
    def search_title(self, title):
        res = [book for book in self.books if Book.title == title]
        if res:
            return f"{Book.author}: {Book.title}"
        else:
            return "Такой книги нету"
        
    def len_books(self, l):    # l mean len
        return f"length: {len(self.books)}"

    def show_books(self):
        for book in self.books:
            print(book)


b1 = Book()
# Создаём книги
b1 = Book("Python", "Tommas")
b2 = Book("C++", "Alice")
b3 = Library()

print(b3.search_author("Tommas"))
    

