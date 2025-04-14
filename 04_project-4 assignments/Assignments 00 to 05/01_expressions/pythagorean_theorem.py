import math  

def main():
    # Get the lengths of the two perpendicular sides from the user
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

   
    bc: float = math.sqrt(ab**2 + ac**2)

    
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")


if __name__ == '__main__':
    main()
