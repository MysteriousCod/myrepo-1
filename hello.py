# addition.py

def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2

def main():
    # Ask for user input
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Add the numbers
        result = add_numbers(number1, number2)
        
        # Print the result
        print(f"The sum of {number1} and {number2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

