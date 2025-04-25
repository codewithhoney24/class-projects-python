# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.



from colorama import Fore, Style, init # type: ignore


init(autoreset=True)

class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        italic = '\033[3m'
        reset = '\033[0m'
        print(Style.BRIGHT + Fore.GREEN + f"{italic}🚗 The {self.brand} car has started! 🚗 🚗 🚗  public_variables_methods.py{reset}")

# Instantiate the class
my_car = Car("Toyota")

# Accessing public variable
italic = '\033[3m'
reset = '\033[0m'
print("\n" + "="*45)
print(Style.BRIGHT + Fore.YELLOW + "*** Public Variables and Methods Example ***\n")
print(Style.BRIGHT + Fore.BLUE + f"{italic}     🛠️    Car Brand : {my_car.brand}   🛠️ {reset}")

# Calling public method
my_car.start()
print("="*45 + "\n")
