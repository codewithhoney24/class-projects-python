# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.



from colorama import init, Fore, Style # type: ignore


init(autoreset=True)

print(Fore.MAGENTA + Style.BRIGHT + "\n=== Custom Exception Example ===\n")

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above."):
        super().__init__(message)


# Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(Fore.RED + f"Invalid age: {age}. Must be 18 or older.")
    else:
        print(Fore.GREEN + f"Age {age} is valid! Access granted.")


# Test the function
try:
    user_age = int(input(Fore.CYAN + "Enter your age: "))
    check_age(user_age)


except InvalidAgeError as e:
    print(Fore.YELLOW + "Custom Exception Caught!")
    print(e)
    

except ValueError:
    print(Fore.RED + "Please enter a valid number.")
