import cmath

def complex_math(x: int, y: int) -> int:
    """Very complex math calculation. This function will add two numbers and return the result of the calculation.

    Args:
        x (int): first number to be calculated.
        y (int): second number to be calculated.

    Returns:
        int: the answer to the calculation.
    """

    answer = x + y

    return answer

def less_complex_math(x: int, y: int) -> int:
    answer = x - y
    
    return answer

def calculate_complex_number(x: int, y: int) -> int:
    complex_number = complex(x,y)
    
    return complex_number