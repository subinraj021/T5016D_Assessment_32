def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Args:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

def main():
    string = input("Enter a string: ")
    
    if is_palindrome(string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()
