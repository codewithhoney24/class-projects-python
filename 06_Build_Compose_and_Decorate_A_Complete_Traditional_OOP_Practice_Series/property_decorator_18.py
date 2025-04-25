# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


from colorama import init, Fore, Style # type: ignore


init(autoreset=True)


print(Fore.MAGENTA + Style.BRIGHT + "\n=== Property Decorators Example ===\n")

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute


    # Getter
    @property
    def price(self):
        print(Fore.CYAN + "Getting the price...")
        return self._price
    

    # Setter
    @price.setter
    def price(self, value):
        if value < 0:
            print(Fore.RED + "Price cannot be negative!")
        else:
            print(Fore.YELLOW + "Setting the price...")
            self._price = value


    # Deleter
    @price.deleter
    def price(self):
        print(Fore.RED + "Deleting the price...")
        del self._price

# Create an instance
product = Product(100)


# Access the price
print(Fore.GREEN + f"Price: {product.price}")


# Update the price
product.price = 150
print(Fore.GREEN + f"Updated Price: {product.price}")


# Try setting a negative price
product.price = -50


# Delete the price
del product.price
