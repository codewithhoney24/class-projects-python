def read_phone_numbers():
    """
    Ask the user for names/numbers to story in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)



if __name__ == '__main__':
    main()



#/////////////////////////////////////   OR   //////////////////////////////////////

# import re  # Import regex module for phone number validation

# def read_phone_numbers():
#     """
#     Ask the user for names/numbers to store in a phonebook (dictionary).
#     Returns the phonebook.
#     """
#     phonebook = {}  # Create empty phonebook

#     while True:
#         name = input("Enter contact name (or press Enter to finish): ").strip()
#         if name == "":
#             break
        
#         # Check if the name already exists
#         if name in phonebook:
#             print(f"{name} already exists. Use 'Edit Contact' to update the number.")
#             continue

#         number = input("Enter phone number: ").strip()
        
#         # Validate phone number format
#         if not re.fullmatch(r'\d{10,15}', number):
#             print("Invalid phone number! Enter 10-15 digits only.")
#             continue

#         phonebook[name] = number

#     return phonebook


# def print_phonebook(phonebook):
#     """
#     Prints out all the names/numbers in the phonebook.
#     """
#     if not phonebook:
#         print("Phonebook is empty.")
#         return

#     print("\nPhonebook Contacts:")
#     for name, number in sorted(phonebook.items()):  # Sort contacts alphabetically
#         print(f"{name} -> {number}")
#     print()


# def lookup_numbers(phonebook):
#     """
#     Allows the user to look up phone numbers in the phonebook.
#     """
#     while True:
#         name = input("Enter name to lookup (or press Enter to exit): ").strip()
#         if name == "":
#             break

#         # Case-insensitive lookup
#         matches = {k: v for k, v in phonebook.items() if k.lower() == name.lower()}
        
#         if matches:
#             for key, value in matches.items():
#                 print(f"{key}: {value}")
#         else:
#             print(f"{name} is not in the phonebook.")


# def edit_contact(phonebook):
#     """
#     Allows the user to update an existing contact's phone number.
#     """
#     name = input("Enter the contact name to edit: ").strip()
#     if name in phonebook:
#         new_number = input(f"Enter new number for {name}: ").strip()
        
#         # Validate phone number format
#         if not re.fullmatch(r'\d{10,15}', new_number):
#             print("Invalid phone number! Enter 10-15 digits only.")
#             return

#         phonebook[name] = new_number
#         print(f"{name}'s number updated successfully!")
#     else:
#         print(f"{name} is not in the phonebook.")


# def delete_contact(phonebook):
#     """
#     Allows the user to delete a contact from the phonebook.
#     """
#     name = input("Enter the contact name to delete: ").strip()
#     if name in phonebook:
#         del phonebook[name]
#         print(f"{name} has been removed from the phonebook.")
#     else:
#         print(f"{name} is not in the phonebook.")


# def main():
#     phonebook = read_phone_numbers()

#     while True:
#         print("\nOptions:")
#         print("1 - View Phonebook")
#         print("2 - Lookup a Number")
#         print("3 - Edit a Contact")
#         print("4 - Delete a Contact")
#         print("5 - Exit")

#         choice = input("Choose an option: ").strip()

#         if choice == "1":
#             print_phonebook(phonebook)
#         elif choice == "2":
#             lookup_numbers(phonebook)
#         elif choice == "3":
#             edit_contact(phonebook)
#         elif choice == "4":
#             delete_contact(phonebook)
#         elif choice == "5":
#             print("Exiting phonebook. Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again!")



# if __name__ == '__main__':
#     main()
