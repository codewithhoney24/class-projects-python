# 11.  Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.



from colorama import init, Fore, Style # type: ignore

# Initialize colorama
init(autoreset=True)


# 🌟 Main Heading
print(Fore.MAGENTA + Style.BRIGHT + "\n========== 📚 WELCOME TO THE BOOK LIBRARY SYSTEM 📚 ==========\n")



class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
        print(Fore.GREEN + f"📚 Book added : {self.title}")

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(Fore.YELLOW + f"Total books so far : {cls.total_books}")
        
        




# Example usage
book1 = Book("Python Basics")

book2 = Book("Advanced Python")

book3 = Book("Data Science with Python")

print(Fore.CYAN + Style.BRIGHT + f"\n📖 Final total books in library : {Book.total_books}")
