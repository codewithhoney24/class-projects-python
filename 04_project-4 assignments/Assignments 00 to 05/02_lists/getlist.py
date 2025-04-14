def main():
    """
    Continuously asks the user for input and adds values to a list.
    Stops when the user presses Enter without typing anything.
    """
    lst = []  # Initialize an empty list

    while True:
        val = input("Enter a value (or press Enter to stop): ").strip()
        if not val:  # Stop when input is empty
            break
        lst.append(val) 

    print("\nHere's the list:", lst)

if __name__ == '__main__':
    main()
