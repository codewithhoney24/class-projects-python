ADULT_AGE: int = 18  # U.S. adult age threshold

def is_adult(age: int) -> bool:
    """Returns True if the person is an adult (18+), otherwise False."""
    return age >= ADULT_AGE

########## No need to edit code beyond this point :) ##########

def main():
    """Gets user input and determines if the person is an adult."""
    while True:
        try:
            age = int(input("How old is this person?: "))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid age.")

    print(is_adult(age))

if __name__ == "__main__":
    main()
