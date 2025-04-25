# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


from colorama import Fore, Style, init # type: ignore


init(autoreset=True)

class Counter:
    # Class variable to track count
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        italic = '\033[3m'
        reset = '\033[0m'

        print("\n" + "="*50)
        print(Style.BRIGHT + Fore.YELLOW + "🧮 Object Creation Counter\n")
        print(Style.BRIGHT + Fore.CYAN + f"{italic}Total Counter Objects Created: {cls.count}{reset}")
        print("="*50 + "\n")


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
obj5 = Counter()

# Display karenga object kitni bar create huye hain
Counter.display_count()
