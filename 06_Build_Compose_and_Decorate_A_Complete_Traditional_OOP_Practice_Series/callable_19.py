# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

from colorama import init, Fore, Style # type: ignore


init(autoreset=True)


print(Fore.MAGENTA + Style.BRIGHT + "\n=== Callable Class Example ===\n")


class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        print(Fore.YELLOW + f"Multiplier created with factor : {self.factor}")


    def __call__(self, value):
        result = self.factor * value
        print(Fore.GREEN + f"Calling object like a function : {self.factor} * {value} = {result}")
        return result

# Create an instance
times3 = Multiplier(3)


# Check if it's callable
print(Fore.CYAN + f"Is 'times3' callable ? {callable(times3)}")



# Call the object like a function
output = times3(10)  # Should print and return 30
