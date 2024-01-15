from enum import Enum

class BookFormat(Enum):
    HARDCOVER = 1,
    PAPERBACK = 2,
    EBOOK = 3,
    AUDIO_BOOK = 4,
    NEWSPAPER = 5,
    MAGZINE = 6,
    JOURNAL = 7


class BookStatus(Enum):
    AVAILABLE = 1,
    RESERVED = 2,
    LOANED = 3,
    LOST = 4

class AccountStatus(Enum):
    ACTIVE = 1,
    CLOSED = 2,
    CANCELED = 3,
    BLACKLISTED = 4,
    NONE = 5

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.cou


class Person:
    def __init__(self, name, age, gender, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone

class Constants:
    self.MAX_BOOKS_ISSUED_TO_USER = 5
    self.MAX_LENDING_DAYS = 10
