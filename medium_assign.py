'''

This file contains the functions that you need for completing this assignment. 

1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''
import math

def expression_1(x):

    '''
        Write a code that returns value for the following expression: x^3 - (2x + x^2) - 100 
    '''

    result = math.pow(x, 3) - ((2 * x) + math.pow(x, 2)) - 100
    return result

def expression_2(x, y):

    '''
        Write code that returns only the integer value of the following expression: (x^4 / 2y) - (3xy) + (6y / 7x)
    '''

    result = (math.pow(x, 4) / (2 * y)) - (3 * x * y) + ((6 * y) / (7 * x))
    return int(result)


def expression_3(x, y):

    '''
        Write code that returns the value of the following expression: (x^3 + y^2) / (x^2 - y^3)
    '''

    result = (math.pow(x, 3) + math.pow(y, 2)) / (math.pow(x, 2) - math.pow(y, 3))
    return result

if __name__ == "__main__":
    
    val_1 = float(input("Enter a number for expression 1: "))
    print(f"The answer to expression 1 is: {expression_1(val_1)}")

    val_2 = float(input("Enter x for expression 2: "))
    val_3 = float(input("Enter y for expression 2: "))
    print(f"The answer to expression 2 is: {expression_2(val_2, val_3)}")

    val_4 = float(input("Enter x for expression 3: "))
    val_5 = float(input("Enter y for expression 3: "))
    print(f"The answer to expression 3 is: {expression_3(val_4, val_5)}")

