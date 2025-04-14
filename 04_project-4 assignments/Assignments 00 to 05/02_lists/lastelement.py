def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print(f"The last element of the list is: {lst[-1]}")

def get_lst():
    """
    Prompts the user to enter list elements one by one.
    Ensures that at least one element is provided.
    """
    lst = []
    while not lst:  # Ensures at least one input
        elem = input("Please enter an element of the list: ").strip()
        while elem:
            lst.append(elem)
            elem = input("Please enter another element (or press Enter to stop): ").strip()
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
