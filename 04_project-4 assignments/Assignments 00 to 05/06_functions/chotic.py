import random  # Importing random module

DONE_LIKELIHOOD = 0.3  # Define the probability of stopping (adjust as needed)

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Stops execution randomly
        print(curr_num)

# Function to randomly decide when to stop counting
def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD  # Returns True if random value is less than likelihood

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
