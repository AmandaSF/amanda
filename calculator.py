"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    expression = read_input()
    tokens = expression.split(" ")
    if tokens[0] == "pow":
        power(int(tokens[1]),int(tokens[2]))
        
    value = evaluate_expression(expression)
    print value


