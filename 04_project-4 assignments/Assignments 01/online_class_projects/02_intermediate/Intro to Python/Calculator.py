# Mars Weight Calculator

# Get user input
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate weight on Mars
mars_weight = round(earth_weight * 0.378, 2)

# Print result
print(f"The equivalent on Mars: {mars_weight}")
