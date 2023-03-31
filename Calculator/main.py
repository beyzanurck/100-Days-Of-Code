from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2): 
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    calculator_continue = "y"
    while calculator_continue == "y":

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        func = operations[operation_symbol]
        result = func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        calculator_continue = input("Do you wanna continue? Type y/n: ")

        if calculator_continue == "y":
            num1 = result
        else:
            calculator()

 
calculator()



