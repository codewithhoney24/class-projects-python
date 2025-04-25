# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
from colorama import Fore, Style, init # type: ignore

# Initialize colorama
init(autoreset=True)


# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclass
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        italic = '\033[3m'
        reset = '\033[0m'
        print(Style.BRIGHT + Fore.GREEN + f"{italic}🟩 Rectangle created with width = {self.width} and height = {self.height}{reset}")

    def area(self):


        italic = '\033[3m'
        reset = '\033[0m'
        result = self.width * self.height
        print(Style.BRIGHT + Fore.BLUE + f"{italic}📏 Area of Rectangle: {result} square units{reset}")

# Demonstration

print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "📐 Abstract Class and Method Demo\n")



# Instantiate Rectangle
rect = Rectangle(10, 5)
rect.area()

print("\n" + "=" * 50)
