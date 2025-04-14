def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(f"The first element of the list is: {lst[0]}")

def get_lst():
    """
    Prompts the user to enter list elements one by one.
    Ensures that at least one element is provided.
    """
    lst = []
    while not lst:  # Keep asking until at least one item is entered
        elem = input("Please enter an element of the list: ").strip()
        while elem:
            lst.append(elem)
            elem = input("Please enter another element (or press Enter to stop): ").strip()
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
