def print_multiple(message: str, repeats: int):
    """Prints the given message the specified number of times."""
    for _ in range(repeats):  # `_` is used since the loop variable isn't needed
        print(message)

# Main function to get user input
def main():
    message = input("Please type a message: ")
    
    # Error handling: Ensure input is a valid integer
    while True:
        try:
            repeats = int(input("Enter a number of times to repeat your message: "))
            if repeats < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print_multiple(message, repeats)

# Ensures main() runs only if the script is executed directly
if __name__ == '__main__':
    main()
