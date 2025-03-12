def basic_calculator():
    """
    A simple calculator program that performs basic arithmetic operations.
    """

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation.")

    except ValueError:
        print("Error: Invalid input. Please enter numbers.")

if __name__ == "__main__":
    basic_calculator()
