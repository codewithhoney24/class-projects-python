# 16.  Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().



from colorama import init, Fore, Style # type: ignore
init(autoreset=True)


print(Fore.MAGENTA + Style.BRIGHT + "\n=== Function Decorator Example ===\n")

# Decorator function
def log_function_call(func):

    def wrapper(*args, **kwargs):
        print(Fore.CYAN + "Function is being called...")
        return func(*args, **kwargs)
    return wrapper


# Apply decorator
@log_function_call
def say_hello():
    print(Fore.GREEN + "Hello, Welcome to python Decorators!")


# Call the function
say_hello()
