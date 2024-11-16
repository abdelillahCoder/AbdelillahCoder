# Program to create a simple calculator that can add, subtract, multiply, and divide using functions

# Define functions for operations
def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides two numbers."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to display the menu of operations
def print_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

# Main program loop
def calculator():
    while True:
        print_menu()
        
        # Get user choice and validate input
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ").strip()

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input! Please choose a valid operation.")
            continue

        # Get and validate the numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")

# Start the calculator
if __name__ == "__main__":
    calculator()
