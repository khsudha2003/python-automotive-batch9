# Define functions for basic arithmetic operations
def add(n1, n2):
    """Adds two numbers and returns the result."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts the second number from the first and returns the result."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers and returns the result."""
    return n1 * n2

def divide(n1, n2):
    """Divides the first number by the second and returns the result. 
    Handles division by zero errors."""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

def calculator():
    """Main calculator function to handle user input and operations."""
    print("Welcome to the Python Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if the choice is valid
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            
            # Ask the user if they want another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                print("Goodbye!")
                break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

# Run the calculator
if __name__ == "__main__":
    calculator()