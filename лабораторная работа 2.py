class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга '{self.name}'"

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

book = Book(id_=1, name='name_1', pages=200)
print(book)  # Выводит: Книга 'name_1'
print(repr(book))  # Выводит: Book(id_=1, name='name_1', pages=200)

class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):
        if len(self.books) > 0:
            last_book = self.books[-1]
            return last_book.id + 1
        else:
            return 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
book_2 = Book(id_=2, name='book2', pages=150)

library = Library([book_2])

print(library.get_next_book_id())  # Выводит: 3
try:
    print(library.get_index_by_book_id(3))  # Вызовет ошибку ValueError
except ValueError as e:
    print(e)  # Выводит: Книги с запрашиваемым id не существует