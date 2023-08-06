def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

print("Simple Calculator")
print("------------------")

while True:
    print("\nOperations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter the operation number (1-5): ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", add(num1, num2))
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", subtract(num1, num2))
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Result: ", multiply(num1, num2))
    elif choice == '4':
        num1 = float(input("Enter the dividend: "))
        num2 = float(input("Enter the divisor: "))
        print("Result: ", divide(num1, num2))
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid input. Please choose a valid operation.")
