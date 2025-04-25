# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.



from colorama import Fore, Style, init # type: ignore

# Initialize colorama
init(autoreset=True)

class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_info(self):
        italic = '\033[3m'
        reset = '\033[0m'
        print(Style.BRIGHT + Fore.CYAN + f"{italic}🏦   Bank Name       : {Bank.bank_name}{reset}")
        print(Style.BRIGHT + Fore.GREEN + f"{italic}👤  Account Holder   : {self.account_holder}{reset}")
        print("-" * 50)

# Create instances
acc1 = Bank("Ali")
acc2 = Bank("Sara")

# Display original bank name
print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.YELLOW + "🏛️ *** Bank System - Before Changing Bank Name ***\n")
acc1.show_info()
acc2.show_info()

# Change bank name using class method
Bank.change_bank_name("Honey National Bank")

# Display updated bank name
print("\n" + "=" * 50)
print(Style.BRIGHT + Fore.MAGENTA + "🏦 *** Bank System - After Changing Bank Name ***\n")
acc1.show_info()
acc2.show_info()
print("=" * 50 + "\n")
