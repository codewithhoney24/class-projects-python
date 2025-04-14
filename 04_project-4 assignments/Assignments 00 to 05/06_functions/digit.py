def print_ones_digit(num: int):
    """Prints the ones digit of the given number."""
    print(f"The ones digit is {num % 10}")

def main():
    """Gets user input and calls print_ones_digit."""
    while True:
        try:
            num = int(input("Enter a number: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    print_ones_digit(num)

# Ensures main() runs only if the script is executed directly
if __name__ == '__main__':
    main()
