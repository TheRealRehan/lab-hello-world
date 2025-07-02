first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number == 0:
        print("Error: You cannot divide by zero.")
    else:
        print(first_number / second_number)
else:
    print("Invalid operation")
    
    