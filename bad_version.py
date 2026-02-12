def calc():
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", x + y)

    elif op == "-":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", x - y)

    elif op == "*":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", x * y)

    elif op == "/":
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", x / y)

    else:
        print("Invalid operation")

calc()
