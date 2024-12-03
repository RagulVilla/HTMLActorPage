def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    """Get a valid arithmetic operator from the user."""
    while True:
        operator = input("Enter the arithmetic operator (+, -, *, /, **): ")
        if operator in ('+', '-', '*', '/', '**'):
            return operator
        print("Invalid operator. Please try again.")

def calculate(a, b, operator):
    """Perform calculation based on the operator."""
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return a / b
        elif operator == '**':
            return a ** b
    except Exception as e:
        print(f"Error during calculation: {e}")
        return None

def calculator_app():
    """Run the calculator app."""
    print("Welcome to the Calculator App!")
    while True:
        # Input first number
        num1 = get_number("Enter the first number: ")

        # Input second number
        num2 = get_number("Enter the second number: ")

        # Input operator
        operator = get_operator()

        # Perform calculation
        result = calculate(num1, num2, operator)
        if result is not None:
            print(f"The result of {num1} {operator} {num2} is: {result}")

        # Ask user if they want to continue
        choice = input("Do you want to perform another calculation? (yes to continue, no to exit): ").strip().lower()
        if choice not in ('yes', 'y'):
            print("Thank you for using the Calculator App. Goodbye!")
            break

# Uncomment the line below to run the calculator app
calculator_app()
