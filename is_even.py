def is_even(number):
    """
    Check if a number is even or odd.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if the number is even, False if odd
    """
    return number % 2 == 0

def print_number_type(number):
    """
    Print whether a number is odd or even.
    
    Args:
        number (int): The number to check
    """
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def main():
    # Test cases
    test_numbers = [4, 7, 10, 13, 20]
    
    for number in test_numbers:
        print_number_type(number)

if __name__ == "__main__":
    main()