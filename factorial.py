def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int: The factorial of the number
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    # Example with two numbers
    num1 = 5
    num2 = 7
    
    # Calculate factorials
    factorial1 = calculate_factorial(num1)
    factorial2 = calculate_factorial(num2)
    
    # Print results
    print(f"Factorial of {num1} is: {factorial1}")
    print(f"Factorial of {num2} is: {factorial2}")

if __name__ == "__main__":
    main()
