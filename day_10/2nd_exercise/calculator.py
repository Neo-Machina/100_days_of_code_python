from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)
    
    while True:
        try:
            num1 = float(input("What's the first number?: "))
            break
        except ValueError:
            print('The typed value ain\'t a number')

    for symbol in operations:
        print(symbol)
        
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        while True:
            try:
                num2 = float(input("What's the next number?: "))
                break
            except ValueError:
                print('The typed value ain\'t a number')

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        keep_calculating = input(
            f'Type \'y\' to continue to calculating with {answer}, or type \'n\' to exit.: '
        )
        if keep_calculating == 'y':
            num1 = answer

        elif keep_calculating == 'n':
            should_continue = False
            calculator()

calculator()