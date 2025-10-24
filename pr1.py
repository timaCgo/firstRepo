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

    def show_books(self):
        for book in self.books:
            print(book)

    

# Создаём книги
b1 = Book("Python", "Tommas")
b2 = Book("C++", "Alice")

# Создаём библиотеку
lib = Library()

# Добавляем книги
lib.add_book(b1)
lib.add_book(b2)

# Проверяем содержимое библиотеки
for book in lib.books:
    print(book)  # выводим статус книги

# Берём книгу
print(lib.borrow_book("Python"))  # Вы взяли книгу: Python
print(lib.borrow_book("Python"))  # Книга уже взята
print(lib.borrow_book("Java")) # Такой книги нет
lib.show_books()

# Проверяем снова статус книг
for book in lib.books:
    print(book)

    

