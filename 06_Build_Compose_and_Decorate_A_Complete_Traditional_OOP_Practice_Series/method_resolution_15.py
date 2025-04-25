# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


from colorama import init, Fore, Style # type: ignore

# Initialize colorama
init(autoreset=True)

# 💎 Main Heading
print(Fore.MAGENTA + Style.BRIGHT + "\n========== 💎 MRO & DIAMOND INHERITANCE DEMO ==========\n")

class A:
    def show(self):
        print(Fore.YELLOW + "🔶 Class A: show() method")

class B(A):
    def show(self):
        print(Fore.BLUE + "🔷 Class B: overridden show() method")



class C(A):
    def show(self):
        print(Fore.CYAN + "🔹 Class C: overridden show() method")



class D(B, C):  # Diamond Inheritance: A <- B & C <- D
    pass

# Creating object of class D
d = D()



# Calling show() to observe Method Resolution Order (MRO)
print(Fore.GREEN + Style.BRIGHT + "\nCalling d.show():")
d.show()

# Displaying MRO order
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n🔍 Method Resolution Order (MRO) for class D:")


for cls in D.__mro__:
    print(Fore.LIGHTWHITE_EX + f"➡️   {cls.__name__}")
