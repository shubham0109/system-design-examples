from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.id = id
        self.password = password
        self.person = person
        self.status = status

    def reset_password(self):
        None

class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super().__init__(id, password, person, status)

    def add_book_item(self, book_item):
        None

    def block_member(self, member):
        None

    def unblock_member(self, member):
        None

class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        

