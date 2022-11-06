def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"Error: {exc}")
        else:
            print(f"Result - {result}")
    return checker

def calculate(expression):
    return eval(expression)

calculate = checker(calculate)
number = input("Write your number:")
number_2 = input("The second number:")
calculate(number + number_2)
