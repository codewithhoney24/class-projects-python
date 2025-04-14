# Define the speed of light constant (m/s)
C: int = 299792458  

def main():
    
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's equation: E = m * c^2
    energy_in_joules: float = mass_in_kg * (C ** 2)


    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")


if __name__ == '__main__':
    main()
