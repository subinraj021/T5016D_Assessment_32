def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
    n (int): The non-negative integer to calculate the factorial for.
    
    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Enter a non-negative integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("The factorial of", number, "is:", factorial(number))

if __name__ == "__main__":
    main()
