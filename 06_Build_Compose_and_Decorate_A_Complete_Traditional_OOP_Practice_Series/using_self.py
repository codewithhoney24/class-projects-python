#  1. Using self
#  Assignment:
#  Create a class Student with attributes name and marks. Use the self keyword to initialize     these values via a constructor. Add a method display() that prints student details.



from colorama import Fore, Style, init # type: ignore

# Initialize colorama
init(autoreset=True)

class Student:
    def __init__(self, name, roll_number, student_class, age, marks):
        self.name = name
        self.roll_number = roll_number
        self.student_class = student_class
        self.age = age
        self.marks = marks

    def display(self):
        italic = '\033[3m'
        reset = '\033[0m'

        print("\n" + "="*50)
        print(Style.BRIGHT + Fore.YELLOW + "*** 🎓 Student Information System 🎓 ***\n")
        print(Style.BRIGHT + Fore.GREEN + f"{italic}(1)  Name         : {self.name}{reset} 👤 ")
        print(Style.BRIGHT + Fore.CYAN + f"{italic}(2)  Roll Number  : {self.roll_number}{reset}  🎟️ ")
        print(Style.BRIGHT + Fore.MAGENTA + f"{italic}(3)  Class        : {self.student_class}{reset} 🏫")
        print(Style.BRIGHT + Fore.LIGHTRED_EX + f"{italic}(4)  Age          : {self.age}{reset} 🎂 ")
        print(Style.BRIGHT + Fore.BLUE + f"{italic}(5)  Marks        : {self.marks}{reset}  📊  ")
        print("="*50 + "\n")

# Example usage
student1 = Student("Ali", "001234", "10th Grade", 16, 85)
student1.display()
