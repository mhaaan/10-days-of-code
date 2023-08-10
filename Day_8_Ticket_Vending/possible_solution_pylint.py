'''
This module contains a simple addition function,
and runs an example showing the result on the screen
'''


def addition(number1, number2):

    """
    This function takes two numeric arguments
    and returns the sum of them
    """

    return number1 + number2


RESULT = addition(5, 7)


print(f'The result of the sum was: {RESULT}')
