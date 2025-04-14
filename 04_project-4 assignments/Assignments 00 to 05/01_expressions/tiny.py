import random

# List of different sentence starters
SENTENCE_STARTS = [
   
    "Today!",
    "I saw a ",
    "I found a ",
    "I heard about a ",
    "I read about a ",
    "I watched a ",
    "I attended a ",
    "you visited a ",
    "we went to a ",
    "they went to a ",
    "he/she/it went to a ",
    "I met a ",
    "you met a ",
    "they met a ",
    "he/she/it met a ",
    "I saw a beautiful ",
    "I saw a stunning ",
    "I saw a magical ",
   
]

def main():
    # Choose a random sentence starter
    SENTENCE_START = random.choice(SENTENCE_STARTS)

    # Get user inputs with validation
    adjective: str = input("Please type an adjective and press enter: ").strip()
    while not adjective:
        adjective = input("Adjective cannot be empty! Please type an adjective: ").strip()

    noun: str = input("Please type a noun and press enter: ").strip()
    while not noun:
        noun = input("Noun cannot be empty! Please type a noun: ").strip()

    verb: str = input("Please type a verb and press enter: ").strip()
    while not verb:
        verb = input("Verb cannot be empty! Please type a verb: ").strip()

    # Print the completed Mad Lib sentence
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == '__main__':
    main()
