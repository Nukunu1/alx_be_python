first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = first + second
        print(f"The result is {result}")
    case '-':
        result = first - second
        print(f"The result is {result}")
    case '*':
        result = first * second
        print(f"The result is {result}")
    case '/':
        if second > 0:
            result = first / second
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero")
