import random  # Import the random module for generating random numbers

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate total of both dice
    total: int = die1 + die2

    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == '__main__':
    main()
