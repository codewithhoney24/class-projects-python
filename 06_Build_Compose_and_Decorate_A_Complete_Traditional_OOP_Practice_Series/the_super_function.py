# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.



from colorama import Fore, Style, init # type: ignore


init(autoreset=True)

class Person:

    def __init__(self, name):

        self.name = name
        italic = '\033[3m'
        reset = '\033[0m'
        print(Style.BRIGHT + Fore.GREEN + f"{italic}Person constructor called for: {self.name}{reset}")



class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling base class constructor
        self.subject = subject
        italic = '\033[3m'
        reset = '\033[0m'

        print(Style.BRIGHT + Fore.BLUE + f"{italic}Teacher constructor called with subject: {self.subject}{reset}")




# Creating a Teacher object

print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "🎓 Demonstrating use of super() in Inheritance\n")

teacher1 = Teacher("Ms. Ayesha", "Mathematics")

print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.CYAN + f"👩 Teacher Info 👩  :\nName   : {teacher1.name} 🏫 \nSubject: {teacher1.subject}")
print("=" * 50 + "\n")
