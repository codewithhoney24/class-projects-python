def get_user_numbers():
    """
    Collects user inputs and returns a list of numbers.
    Continues until the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    return user_numbers


def count_nums(num_lst):
    """
    Returns a dictionary with counts of each number in the list.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def print_counts(num_dict):
    """
    Prints the occurrences of each number in the list.
    """
    for num, count in sorted(num_dict.items()):  # Sorted for better readability
        print(f"{num} appears {count} times.")


def main():
    """
    Main function that collects numbers, counts occurrences, and prints the results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


if __name__ == '__main__':
    main()
