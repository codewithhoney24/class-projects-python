# Planetary Weight Calculator

# Dictionary storing gravity multipliers for planets
gravity_multipliers = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get user input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Calculate and display the weight on the chosen planet
if planet in gravity_multipliers:
    planetary_weight = round(earth_weight * gravity_multipliers[planet], 2)
    print(f"The equivalent weight on {planet}: {planetary_weight}")
else:
    print("Invalid planet name. Please enter a correct planet name from the list.")
