def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
    number (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    number = int(input("Enter a number: "))
    
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

if __name__ == "__main__":
    main()
