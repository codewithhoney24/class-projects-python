
AURORA_LICENSE_AGE: int = 16
VERDANIA_LICENSE_AGE: int = 18
ELDRIS_LICENSE_AGE: int = 25

def main():
    
    user_age = int(input("How old are you? "))

    
    if user_age >= AURORA_LICENSE_AGE:
        print("You can apply for a driving license in Aurora at age " + str(AURORA_LICENSE_AGE) + ".")
    else:
        print("You cannot apply for a driving license in Aurora until you are " + str(AURORA_LICENSE_AGE) + ".")

    
    if user_age >= VERDANIA_LICENSE_AGE:
        print("You can apply for a driving license in Verdania at age " + str(VERDANIA_LICENSE_AGE) + ".")
    else:
        print("You cannot apply for a driving license in Verdania until you are " + str(VERDANIA_LICENSE_AGE) + ".")

    # Check if the user can get a driving license in Eldris
    if user_age >= ELDRIS_LICENSE_AGE:
        print("You can apply for a driving license in Eldris at age " + str(ELDRIS_LICENSE_AGE) + ".")
    else:
        print("You cannot apply for a driving license in Eldris until you are " + str(ELDRIS_LICENSE_AGE) + ".")


if __name__ == '__main__':
    main()
