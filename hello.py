# addition.py

def add_numbers(num1, num2, num3):
    """Function to add two numbers."""
    return num1 + num2 + num3

def main():
    # Ask for user input
    try:
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        number3 = int(input("Enter the third number: ")) 
        # Add the numbers
        result = add_numbers(number1, number2, number3)
        
        # Print the result
        print(f"The sum of {number1} and {number2} and {number3} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

