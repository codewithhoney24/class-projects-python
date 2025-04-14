import random  # Correct import

# Define the number of sides on the dice
NUM_SIDES = 6

def main():
    print("Starting the dice rolling simulation...")  

    die1 = random.randint(1, NUM_SIDES)  # No need for type: ignore
    die2 = random.randint(1, NUM_SIDES)  
    total = die1 + die2

    print(f"Rolled: {die1} and {die2} (Total: {total})")  


if __name__ == "__main__":
    main()
