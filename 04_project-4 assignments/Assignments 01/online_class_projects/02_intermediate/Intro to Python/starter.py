"""
Prompts the user for a weight on Earth
and a planet, then prints the equivalent weight on that planet.
"""

# Gravity multipliers for each planet
GRAVITY_MULTIPLIERS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the planet
    planet = input("Enter a planet: ")

    # Check if the planet exists in the dictionary
    if planet in GRAVITY_MULTIPLIERS:
        # Calculate the equivalent weight
        planetary_weight = round(earth_weight * GRAVITY_MULTIPLIERS[planet], 2)
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a correct planet name.")

if __name__ == "__main__":
    main()
