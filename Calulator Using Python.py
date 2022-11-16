# Calculator using Python

# define all the operations
def addition(x, y):
    return x+y


def substraction(x, y):
    return x-y


def division(x, y):
    return x/y


def multiplication(x, y):
    return x*y


# exaplin the operations using dictionary
operation = {
    "+": addition,
    "-": substraction,
    "/": division,
    "*": multiplication
}


def calculator():                                     # Recursion function(A function that calls itself)
    num1 = float(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation from the line above: ")
        num = float(input("Enter the next number: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num)

        print(f"{num1} {operation_symbol} {num} = {answer}")

        if (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y'):
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
