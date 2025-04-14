import random

NUM_ROUNDS = 5

def play_game():
    print("Welcome to the High-Low Game! 🎲")
    print("-" * 40)

    your_score = 0  # Keeps track of the player's score

    for i in range(NUM_ROUNDS):
        print(f"🔹 Round {i + 1}")
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print(f"🎯 Your number is {your_num}")

        # Get user input and validate it
        choice = input("Do you think your number is 'higher' or 'lower' than the computer's?: ").strip().lower()
        while choice not in ["higher", "lower"]:
            choice = input("❌ Invalid choice! Please enter 'higher' or 'lower': ").strip().lower()

        # Check if the user guessed correctly
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print(f"✅ Correct! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"❌ Wrong! The computer's number was {computer_num}.")

        print(f"📊 Your current score: {your_score}\n")

    # Final score and performance message
    print("🎮 Game Over!")
    print(f"🏆 Your final score is: {your_score}/{NUM_ROUNDS}")

    if your_score == NUM_ROUNDS:
        print("🔥 Perfect score! You're a pro! 🎉")
    elif your_score > NUM_ROUNDS // 2:
        print("👍 Great job! You did really well! 🎯")
    else:
        print("😢 Better luck next time!")

    return your_score  # Return the final score for high-score tracking

def main():
    high_score = 0  # Track the highest score across games

    while True:
        score = play_game()
        high_score = max(high_score, score)  # Update high score

        print(f"\n🏅 Highest Score So Far: {high_score}/{NUM_ROUNDS}")

        # Ask if the player wants to play again
        play_again = input("🔄 Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! See you next time! 🎉")
            break

if __name__ == "__main__":
    main()
