def main():
    
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    #  remainder
    quotient: int = dividend // divisor  # Integer division (floor division)
    remainder: int = dividend % divisor  # Modulo operation for remainder

    print(f"The result of this division is {quotient} with a remainder of {remainder}")



if __name__ == '__main__':
    main()
