import re

def get_user_data():
    """
    Asks the user for their first name, last name, and email address.
    Ensures valid inputs before returning the data.
    """
    # Validate first name
    while True:
        first_name = input("What is your first name?: ").strip()
        if first_name.isalpha():
            break
        print("Invalid input! Please enter only letters for your first name.")

    # Validate last name
    while True:
        last_name = input("What is your last name?: ").strip()
        if last_name.isalpha():
            break
        print("Invalid input! Please enter only letters for your last name.")

    # Validate email format
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email_address = input("What is your email address?: ").strip()
        if re.match(email_pattern, email_address):
            break
        print("Invalid email! Please enter a valid email address.")

    return first_name, last_name, email_address  # Returns a tuple


def display_user_data(first_name, last_name, email_address):
    """
    Nicely formats and prints the collected user information.
    """
    print("\n✅ **User Registration Successful!** ✅")
    print("=" * 40)
    print(f"📌 First Name  : {first_name}")
    print(f"📌 Last Name   : {last_name}")
    print(f"📌 Email       : {email_address}")
    print("=" * 40)


def main():
    first, last, email = get_user_data()  # Tuple unpacking
    display_user_data(first, last, email)  # Display user data in a structured format


if __name__ == "__main__":
    main()
