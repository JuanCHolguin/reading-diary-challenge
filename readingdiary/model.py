from datetime import datetime

class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str= text
        self.page: int = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"

class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note (self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        else:
            note = Note(text, page, date)
            self.notes.append(note)
        return True

    def set_rating (self, rating: int) -> bool:
        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page (self, page: int) -> list[Note]:
        nota_obtenida = []
        for notes in self.notes:
            if notes.page == page:
                nota_obtenida.append(notes)
        return nota_obtenida

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        contador = {}

        for note in self.notes:
            if note.page in contador:
                contador[note.page] += 1
            else:
                contador[note.page] = 1

        return max(contador, key=contador.get)

    def __str__ (self) -> str:
        ratings = {
            Book.EXCELLENT: "excellent",
            Book.GOOD: "good",
            Book.BAD: "bad",
            Book.UNRATED: "unrated"
        }
        rating = ratings[self.rating]

        return f"ISBN: {self.isbn}\nTitle: {self.title}\nAuthor: {self.author}\nPages: {self.pages}\nRating: {rating}"

class ReadingDiary:
    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book (self, isbn: str, title: str, author: str, pages: int) -> bool:

        if isbn in self.books:
            return False
        book = Book(isbn, title, author, pages)
        self.books[isbn] = book

        return True

    def search_by_isbn (self, isbn: str) -> Book | None:
        if isbn in self.books:
            return self.books[isbn]
        return None

    def add_note_to_book (self, isbn: str, text: str, page: int, date: datetime) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.set_rating(rating)

    def book_with_most_notes (self) -> Book | None:





