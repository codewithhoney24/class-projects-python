import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize player score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers
        user_number = random.randint(MIN_VALUE, MAX_VALUE)
        computer_number = random.randint(MIN_VALUE, MAX_VALUE)

        print(f"Your number is {user_number}")
        
        # Get user input and validate it
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()
        
        # Determine if the guess is correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")
            score += 1  # Increase score if correct
        else:
            print("Aww, that's incorrect.", end=" ")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")  # Show updated score

    # End game message based on performance
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
