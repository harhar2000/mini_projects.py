# Write a function for a basic calculator that allows a user to:

# Choose an operator (+, -, *, /).
# Input two numbers.
# Perform the selected operation on the two numbers and print the result rounded to three decimal places.
# Handle invalid operator input by displaying an error message."


def calculator():
    operator = input("Choose your operator (+ - * /): ")
    num1 = float(input("Choose a number: "))
    num2 = float(input("Choose a number: "))

    if operator == "+": 
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-": 
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*": 
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/": 
        result = num1 / num2
        print(round(result, 3))
    else:
        print(f"{operator} is not a valid operator ")
    

calculator()