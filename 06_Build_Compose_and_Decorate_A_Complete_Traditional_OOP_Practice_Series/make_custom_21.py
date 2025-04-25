#  21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


from colorama import init, Fore, Style # type: ignore


init(autoreset=True)

print(Fore.MAGENTA + Style.BRIGHT + "\n=== Custom Iterable: Countdown ===\n")

# Custom Iterable Class
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start


    def __iter__(self):
        self.current = self.start  # Reset the counter for iteration
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value
        

# Create an instance
countdown = Countdown(5)


# Iterate using a for-loop
for num in countdown:
    print(Fore.CYAN + f"Countdown : {num}")
