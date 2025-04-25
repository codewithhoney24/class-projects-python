# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


from colorama import init, Fore, Style # type: ignore


init(autoreset=True)


print(Fore.MAGENTA + Style.BRIGHT + "\n=== Class Decorator Example ===\n")

# Class decorator
def add_greeting(cls):
    def greet(self):
        return Fore.GREEN + "Hello from Decorator!"
    cls.greet = greet
    return cls



# Apply the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an instance of Person
person1 = Person("Zain Ahmed")

# Call the added method
print(Fore.CYAN + f"{person1.name} says  :", person1.greet())
