num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = str(input("Choose the operation (+, -, *, /): "))

match operation:
    case "+": # Addition operation
        result = num1 + num2
    case "-": # Subtraction operation
        result = num1 - num2
    case "*": # Multiplication operations
        result = num1 * num2
    case "/": # The division operations
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero")
            result = False     
    case _:
        print("Operation is unknown")
print(f"The result is {result}")