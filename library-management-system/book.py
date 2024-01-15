
class Book:
    def __init__(self, name, isbn, publication_year, publisher, no_of_pages, subject):
        self.name = name
        self.isbn = isbn
        self.publisher = publisher
        self.publication_year = publication_year
        self.no_of_pages = no_of_pages
        self.subject = subject
        self.authors = []

class BookItem(Book):
    def __init__(self, name, isbn, publication_year, publisher, no_of_pages, subject):
        super().__init__(name, isbn, publication_year, publisher, no_of_pages, subject)

    def add_author(self, author_name):
        self.authors.append(author_name)

