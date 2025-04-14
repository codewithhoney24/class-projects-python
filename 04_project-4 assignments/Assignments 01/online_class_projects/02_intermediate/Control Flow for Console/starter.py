import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game! 🎲")
    print('-' * 40)

    your_score = 0  # Track user's score

    for i in range(NUM_ROUNDS):
        print(f"🔹 Round {i + 1}")

        # Generate random numbers
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"🎯 Your number is {your_num}")

        # Get user choice
        choice = input("Do you think your number is 'higher' or 'lower' than the computer's?: ").strip().lower()
        
        # Validate input
        while choice not in ["higher", "lower"]:
            choice = input("❌ Invalid choice! Please enter 'higher' or 'lower': ").strip().lower()

        # Check if the user guessed correctly
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print(f"✅ Correct! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"❌ Wrong! The computer's number was {computer_num}.")

        print(f"📊 Your current score: {your_score}\n")

    # Final score message
    print("🎮 Game Over!")
    print(f"🏆 Your final score is: {your_score}/{NUM_ROUNDS}")

    if your_score == NUM_ROUNDS:
        print("🔥 Perfect score! You're a pro! 🎉")
    elif your_score > NUM_ROUNDS // 2:
        print("👍 Great job! You did really well! 🎯")
    else:
        print("😢 Better luck next time!")

if __name__ == "__main__":
    main()
