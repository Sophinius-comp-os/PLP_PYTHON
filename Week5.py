# Assignment 1: Design Your Own Class - Book

class Book:
    """Represents a book with title, author, and page count."""

    def __init__(self, title, author, pages):
        """Initializes a Book object."""
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    def read_page(self):
        """Simulates reading a page."""
        if self.current_page <= self.pages:
            print(f"Reading page {self.current_page} of '{self.title}'.")
            self.current_page += 1
        else:
            print(f"You've finished reading '{self.title}'.")

    def get_progress(self):
        """Returns the current reading progress."""
        progress = (self.current_page - 1) / self.pages * 100
        return f"You've read {progress:.2f}% of '{self.title}'."

class EBook(Book):
    """Represents an electronic book, inheriting from Book."""

    def __init__(self, title, author, pages, file_format):
        """Initializes an EBook object."""
        super().__init__(title, author, pages)
        self.file_format = file_format
        self.battery_level = 100

    def download(self):
        """Simulates downloading an eBook."""
        print(f"Downloading '{self.title}' in {self.file_format} format...")

    def read_page(self):
        """Overrides read_page to include battery usage."""
        if self.battery_level > 0:
            super().read_page()
            self.battery_level -= 1
            print(f"Battery level: {self.battery_level}%")
        else:
            print("Battery depleted. Please charge your device.")

# Activity 2: Polymorphism Challenge - Animals

class Animal:
    """Base class for animals."""

    def move(self):
        """Generic move method."""
        print("This animal moves.")

class Dog(Animal):
    """Dog class, inheriting from Animal."""

    def move(self):
        """Dog-specific move method."""
        print("Running and wagging tail! 🐾")

class Fish(Animal):
    """Fish class, inheriting from Animal."""

    def move(self):
        """Fish-specific move method."""
        print("Swimming in the water! 🐟")

class Bird(Animal):
    """Bird class, inheriting from Animal."""

    def move(self):
        """Bird-specific move method."""
        print("Flying in the sky! 🐦")

# Example Usage
if __name__ == "__main__":
    # Assignment 1
    my_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
    my_ebook = EBook("Dune", "Frank Herbert", 896, "epub")

    my_book.read_page()
    print(my_book.get_progress())

    my_ebook.download()
    for _ in range(5):
      my_ebook.read_page()

    # Activity 2
    dog = Dog()
    fish = Fish()
    bird = Bird()

    animals = [dog, fish, bird]

    for animal in animals:
        animal.move()
