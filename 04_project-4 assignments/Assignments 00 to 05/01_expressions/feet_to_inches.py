# Define the conversion factor (12 inches per foot)
INCHES_IN_FOOT: int = 12  

def main():
    # Get the number of feet from the user
    feet: float = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT  

    # Display the result
    print(f"{feet} feet is equal to {inches} inches.")

# Run the program
if __name__ == '__main__':
    main()
