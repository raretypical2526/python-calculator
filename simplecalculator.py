# This is a simple calculator that performs basic operations
num1= int(input("Enter a number:"))
operation = input("Enter an operation:")
num3 = int(input("Enter another number:"))
if operation == "+":
    print(num1 + num3)
elif operation == "-":
    print(num1 - num3)
elif operation == "/":
    print(num1 / num3)
elif operation == "*":
    print(num1 * num3)
elif operation == "**":
    print(num1 ** num3)
elif operation == "//":
    print(num1 // num3)
elif operation == "%":
    print(num1 % num3)
else:
    print("Invalid operator")