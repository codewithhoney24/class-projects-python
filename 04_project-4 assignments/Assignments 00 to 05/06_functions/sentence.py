def make_sentence(word: str, part_of_speech: int):
    """Generates a sentence based on the given word and part of speech."""
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

# Main function to get user input
def main():
    word = input("Please type a noun, verb, or adjective: ")

    # Validate user input for part_of_speech
    while True:
        try:
            part_of_speech = int(input("Is this a noun, verb, or adjective?\nType 0 for noun, 1 for verb, 2 for adjective: "))
            if part_of_speech in [0, 1, 2]:
                break
            else:
                print("Invalid choice! Please enter 0 for noun, 1 for verb, or 2 for adjective.")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")

    make_sentence(word, part_of_speech)

# Ensures main() runs only if the script is executed directly
if __name__ == '__main__':
    main()
