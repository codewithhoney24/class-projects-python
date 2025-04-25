# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


from colorama import Fore, Style, init # type: ignore

# Initialize colorama
init(autoreset=True)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Example usage
num1 = 25
num2 = 35
result = MathUtils.add(num1, num2)

# Stylish output
italic = '\033[3m'
reset = '\033[0m'

print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "📐 Math Utils - Static Method Example\n")
print(Style.BRIGHT + Fore.CYAN + f"{italic}Adding {num1} and {num2} gives: {result}{reset}")
print("=" * 50 + "\n")
