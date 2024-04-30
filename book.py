class Book:

    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __eq__(self, value: object) -> bool:
        return self.title == value.title and self.author == value.author

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
book1 = Book("Title1", "Author1")
book2 = Book("Title2", "Author2")

print(book1 == book2)
print(book1 != book2)