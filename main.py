print("Welcome to khushi's calculator")
from art import logo
import math

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def exponentiation(n1, n2):
    return n1 ** n2

def modulo(n1, n2):
    return n1 % n2

def square_root(n):
    return math.sqrt(n)

def percentage(n, percent):
    return n * (percent / 100)

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "^": exponentiation,
    "%": modulo,
    "sqrt": square_root,
    "perc": percentage,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan
}

def cal():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation.")
            continue
        if operation_symbol in ["sqrt", "perc", "sin", "cos", "tan"]:
            num2 = None
        else:
            num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        if num2 is None:
            answer = calculation_function(num1)
            print(f"{operation_symbol}({num1}) = {answer}")
        else:
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") != "y":
            should_continue = False
            cal()
        else:
            num1 = answer

cal()
