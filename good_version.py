'''
:author: Varun Venkatadri
:author: Abrar Ferdou

Simple Calculator

'''

def add(num1:float, num2:float) -> float:
    '''
    Add 2 floats
    
    :param num1: First number to be added
    :type num1: float
    :param num2: Second number to be added
    :type num2: float
    :return: Sum of num1 and num2
    :rtype: float
    '''
    return num1 + num2


def subtract(num1:float, num2:float) -> float:
    '''
    Subtract 2 floats
    
    :param num1: First number to be subtracted
    :type num1: float
    :param num2: Second number to be subtracted
    :type num2: float
    :return: Difference between num1 and num2
    :rtype: float
    '''
    
    return num1 - num2


def multiply(num1:float, num2:float) -> float:
    '''
    Multiply 2 floats
    
    :param num1: First number to be multiplied
    :type num1: float
    :param num2: Second number to be multiplied
    :type num2: float
    :return: Product of num1 and num2
    :rtype: float
    '''
    
    return num1 * num2


def divide(num1:float, num2:float) -> float:
    '''
    Divide 2 floats
    
    :param num1: First number to be divided; dividend
    :type num1: float
    :param num2: Second number to be divided; divisor
    :type num2: float
    :return: Quotient of num1 divided by num2
    :rtype: float
    '''
    
    return num1 / num2


def get_inputs() -> tuple[float, float]:
    '''
    Get float inputs from user
    
    :return: tuple of input floats in the order they were entered by the user 
    :rtype: tuple[float, float]
    '''
    
    num1:float = float(input("Enter first number: "))
    num2:float = float(input("Enter second number: "))
    
    return (num1, num2)
        
    
def calc(num1:float, num2:float) -> tuple[float, bool]:
    '''
    Calculate result of operation with 2 floats
    
    :param num1: 1st operand
    :type num1: float
    :param num2: 2nd operand
    :type num2: float
    :return: (operation solution, success of function)
    :rtype: tuple[float, bool]
    '''
    
    result:tuple[float,bool] = (0, False)
    
    solution:float = 0
    
    operation:str = input("Choose operation (+, -, *, /): ")
    
    match (operation):
        case "+":
            solution = add(num1, num2)
        case "-":
            solution = subtract(num1, num2)
        case "*":
            solution = multiply(num1, num2)
        case "/":
            solution = divide(num1, num2)
        case _:
            return result
    
    result = (solution, True)
    
    return result
