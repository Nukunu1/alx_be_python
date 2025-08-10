# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = year
        self._is_checked_out = False  # not used here, but OK to include

    def __str__(self):
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: print deletion message when object is deleted."""
        # Must match exact expected output: "Deleting 1984"
        print(f"Deleting {self.title}")
