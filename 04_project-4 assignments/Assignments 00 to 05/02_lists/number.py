def add_many_numbers(numbers: list[int]) -> int:
    """Returns the sum of a list of numbers."""
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number  # Summing up numbers in the list
    return total_so_far

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum

if __name__ == '__main__':
    main()


# ////////////////////////////    OR   ////////////////////////////

#     def add_many_numbers(numbers: list[int]) -> int:
#     """Returns the sum of a list of numbers."""
#     return sum(numbers)

# def main():
#     numbers = [1, 2, 3, 4, 5]
#     print(add_many_numbers(numbers))

# if __name__ == '__main__':
#     main()

