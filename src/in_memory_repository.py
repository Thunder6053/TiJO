from library_repository import LibraryRepository

class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self.books = {}  # klucz: tytuł, wartość: (autor, rok)

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = (author, year)

    def remove_book(self, title: str) -> bool:
        if title in self.books:
            del self.books[title]
            return True
        return False

    def get_all_books(self) -> list:
        return [(title, *details) for title, details in self.books.items()]