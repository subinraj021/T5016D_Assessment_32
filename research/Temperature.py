def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
    celsius (float): Temperature in Celsius.
    
    Returns:
    float: Temperature converted to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Args:
    fahrenheit (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * 5/9

def main():
    choice = input("Enter 'C' to convert Celsius to Fahrenheit, 'F' to convert Fahrenheit to Celsius: ").upper()
    
    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
