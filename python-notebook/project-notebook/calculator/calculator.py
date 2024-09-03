from exceptions import IncorrectOperatorError, InvalidEquationError
import re as regex

"""
v1.0: Current version is only good to calculate the single equation. i.e. a + b
v2.0: Multiple equations
v3.0: Brackets
"""


def equate(equation: str) -> str:
    """
    To perform the operation on the numbers using associated operators in the provided equation
    :param equation: to evaluate
    :return: floating point number which is the result of the equation
    """
    result = 0.0
    if is_valid_equation(equation):
        split_equation = regex.split(' ', equation)
        result += run(split_equation[1], float(split_equation[0]), float(split_equation[2]))
        return format(result, '.2f')
    else:
        raise InvalidEquationError(f'Invalid equation provided: {equation}')


def is_valid_equation(equation: str) -> bool:
    """
    To check that the provided equation is correct or not
    :param equation:
    :return:
    """
    pattern = regex.compile(validation_regex())
    return bool(regex.search(pattern, equation))


def validation_regex() -> str:
    """
    This is the most critical and ever evolving piece of code to determine if the provided equation is correct or not.
    I'll keep on modifying it until it correctly recognises the correct pattern.
    :return: The regex pattern to determine the correctness of the equation.
    """
    return '^[0-9+\\-*/.\\s]+$'


def run(operator: str, number_a: float, number_b: float) -> float:
    """
    Calculate the result of the two numbers basis the provided operation
    :param operator: defines the operator to use for evaluation
    :param number_a: first number to perform operation with
    :param number_b: second number to perform operation with
    :return: the result in the floating point
    """
    match operator:
        case '+':
            return number_a + number_b
        case '-':
            return number_a - number_b
        case '*':
            return number_a * number_b
        case '/':
            return number_a / number_b
        case default:
            raise IncorrectOperatorError(f'Incorrect operator: {default} found')


if __name__ == '__main__':
    user_equation_input = input('Enter your equation: ')
    print(f'Result: {equate(user_equation_input)}')
