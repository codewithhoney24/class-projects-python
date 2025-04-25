#  Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).



from colorama import Fore, Style, init # type: ignore
import time

# Initialize colorama
init(autoreset=True)

class Logger:
    def __init__(self):
        italic = '\033[3m'
        reset = '\033[0m'
        print(Style.BRIGHT + Fore.GREEN + f"{italic}🟢 Logger object has been created.{reset}")


    def __del__(self):

        # ANSI escape codes for colors and styles
        italic = '\033[3m'
        reset = '\033[0m'

        # This method is called when the object is about to be destroyed
        print(Style.BRIGHT + Fore.RED + f"{italic}🔴 Logger object has been destroyed.{reset}")

# Main script to demonstrate the constructor and destructor
print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "📘 Constructor & Destructor Demo\n")



logger1 = Logger()  # Constructor is called



print(Style.BRIGHT + Fore.CYAN + "⌛ Doing some work with the logger...\n")
time.sleep(2)  # Simulate some delay



print(Style.BRIGHT + Fore.MAGENTA + "🧹 Logger object will be deleted manually...\n")
del logger1  # Destructor is called manually here

print("=" * 50 + "\n")
