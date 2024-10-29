# Calculator which takes 
#
# Asks for an operator
# Enter 1st / 2nd number string
# print result




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