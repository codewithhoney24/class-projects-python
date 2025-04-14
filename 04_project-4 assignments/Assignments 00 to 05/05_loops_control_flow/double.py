def main():
    """
    This function asks the user for a number, then repeatedly doubles it until it reaches 100 or more.
    """
    curr_value = int(input("Enter a number: "))  # Get user input and convert to integer

    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value)  # Print the updated value



if __name__ == '__main__':
    main()
