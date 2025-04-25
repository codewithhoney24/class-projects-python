# # 10.  Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

from colorama import Fore, Style, init # type: ignore



init(autoreset=True)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        italic = '\033[3m'
        reset = '\033[0m'


        print(Style.BRIGHT + Fore.GREEN + f"{italic}🐾 A new dog has been created!{reset}")
        print(Style.BRIGHT + Fore.CYAN + f"{italic}Name : {self.name}{reset}")
        print(Style.BRIGHT + Fore.MAGENTA + f"{italic}Breed: {self.breed}{reset}")



    def bark(self):
        italic = '\033[3m'
        reset = '\033[0m'


        print(Style.BRIGHT + Fore.YELLOW + f"{italic}🔊 {self.name} says: Woof! Woof!{reset}")



# Create an instance of Dog
print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.BLUE + "🐶 Dog Class with Instance Method\n")

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()

print("\n" + "=" * 50)
