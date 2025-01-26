# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor to initialize the Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the book instance for end users.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the book instance for developers.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
