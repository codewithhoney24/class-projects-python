def add_three_copies(my_list, data):
    my_list.extend([data] * 3)  # More efficient and concise

    def change_number(x):
     x += 3  # This does NOT affect the original variable outside the function

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

    # Demonstrating immutability
    num = 5
    print("\nNumber before:", num)
    change_number(num)
    print("Number after:", num)  # Still 5, because integers are immutable!

if __name__ == "__main__":
    main()

