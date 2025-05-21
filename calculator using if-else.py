num1 = float(input("Enter first number: "))
opr = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if opr == '+':
    result = num1 + num2
    print("Result:", result)
elif opr == '-':
    result = num1 - num2
    print("Result:", result)
elif opr == '*':
    result = num1 * num2
    print("Result:", result)
elif opr == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")
