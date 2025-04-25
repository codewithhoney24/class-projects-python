# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.




from colorama import Fore, Style, init # type: ignore

# Initialize colorama
init(autoreset=True)

class Employee:

    def __init__(self, name, salary, ssn):
        self.name = name            # Public
        self._salary = salary       # Protected
        self.__ssn = ssn            # Private
        

    def display(self):
        italic = '\033[3m'
        reset = '\033[0m'


        print(Style.BRIGHT + Fore.GREEN + f"{italic}Public Name       : {self.name}{reset}")
        print(Style.BRIGHT + Fore.BLUE + f"{italic}Protected Salary  :  {self._salary}{reset}")
        print(Style.BRIGHT + Fore.RED + f"{italic}Private SSN       :  {self.__ssn}{reset}")




# Create an object


emp = Employee("Ali Raza", 75000, "123-45-6789")

print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "*** 🔐 Access Modifiers in Python***\n")



# Accessing variables
italic = '\033[3m'
reset = '\033[0m'



print(Style.BRIGHT + Fore.CYAN + f"{italic}*** Accessing from inside the class:{reset}")


emp.display()


print("\n" + "-" * 50)
print(Style.BRIGHT + Fore.MAGENTA + f"{italic}Accessing from outside the class:{reset}\n")



# Public access
print(Style.BRIGHT + Fore.GREEN + f"{italic}✅   Public Name: {emp.name}{reset}")

# Protected access
print(Style.BRIGHT + Fore.BLUE + f"{italic}⚠️    Protected Salary (should be accessed within class or subclass): {emp._salary}{reset}")

# Private access (will fail if accessed directly)
try:
    print(Style.BRIGHT + Fore.RED + f"{italic}❌  Private SSN: {emp.__ssn}{reset}")


except AttributeError as e:
    print(Style.BRIGHT + Fore.RED + f"{italic}❌   Cannot access private variable directly: {e}{reset}")



# Accessing private variable using name mangling (not recommended)



print(Style.BRIGHT + Fore.YELLOW + f"{italic}🛠️    Accessing private SSN using name mangling: {emp._Employee__ssn}{reset}")

print("=" * 50 + "\n")
