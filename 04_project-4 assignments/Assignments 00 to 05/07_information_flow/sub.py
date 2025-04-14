def subtract_seven(num: int) -> int:
    """
    Subtracts 7 from the given number and returns the result.
    """
    return num - 7


def main():
    number = int(input("Enter a number: "))  # User-defined input
    result = subtract_seven(number)
    print(f"Result after subtracting 7: {result}")



if __name__ == '__main__':
    main()
