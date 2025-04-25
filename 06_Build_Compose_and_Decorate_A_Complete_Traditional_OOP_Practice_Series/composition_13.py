# Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


from colorama import init, Fore, Style # type: ignore


init(autoreset=True)

# 🚘 Main Heading
print(Fore.MAGENTA + Style.BRIGHT + "\n========== 🚘 CAR & ENGINE COMPOSITION SYSTEM ==========\n")

class Engine:
    def start(self):
        return Fore.YELLOW + "🔧 Engine started..."
    
    

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car HAS-A Engine



    def start_car(self):
        return self.engine.start() + Fore.GREEN + " 🚗🚗🚗🚗🚗🚗🚗  Cars is ready to go!"

# Creating Engine object
my_engine = Engine()




# Passing Engine object to Car

my_car = Car(my_engine)

# Using method via Car
print(my_car.start_car())
