from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    nums = Stack(30)
    tokens = input_str.split()
    int_count = 0
    op_count = 0
    #First for loop tries to catch errors like invalid token, insufficient operands and too many operands.
    for i in range(len(tokens)):
        if (tokens[i] not in '0-1-2-3-4-5-6-7-8-9 + - / * >> << **') and (not is_float(tokens[i])):
            raise PostfixFormatException("Invalid token")
        if tokens[i] in "+ - / * << >> **":
            op_count += 1
        else:
            int_count += 1
    if int_count <= op_count:
        raise PostfixFormatException("Insufficient operands")
    if int_count >= (op_count + 2):
        raise PostfixFormatException("Too many operands")
    #Second for loop evaluates postfix expression step by step.
    for i in range(len(tokens)):
        if tokens[i] in "- + / * << >> **":
            op2 = nums.pop()
            op1 = nums.pop()
            if tokens[i] == "+":
                result = op1 + op2
            elif tokens[i] == "-":
                result = op1 - op2
            elif tokens[i] == "*":
                result = op1 * op2
            elif tokens[i] == "/":
                if op2 == 0:
                    raise ValueError
                result = op1/op2
            elif tokens[i] == "**":
                result = op1**op2
            elif tokens[i] == "<<":
                if not op1.is_integer() or not op2.is_integer():
                    raise PostfixFormatException("Illegal bit shift operand")
                result = op1 * (2 ** op2)
            else:
                if not op1.is_integer() or not op2.is_integer():
                    raise PostfixFormatException("Illegal bit shift operand")
                result = op1 / (2 ** op2)
            nums.push(result)
        else:
            nums.push(float(tokens[i]))
    return nums.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    #Create a dictionary that stores the precendence of each operator.
    order = {}
    order[">>"] = 5
    order["<<"] = 5
    order["**"] = 4
    order["*"] = 3
    order["/"] = 3
    order["+"] = 2
    order["-"] = 2
    order["("] = 1
    nums = Stack(30)
    pfixlist = []
    tokens = input_str.split()
    for i in range(len(tokens)):
        if tokens[i] == "**" and nums.peek() == "**":
            nums.push(tokens[i])
        elif tokens[i] in "- + * / ** << >>":
            while (not nums.is_empty()) and (order[nums.peek()] >= order[tokens[i]]):
                pfixlist.append(nums.pop())
            nums.push(tokens[i])
        elif tokens[i] == "(":
            nums.push(tokens[i])
        elif tokens[i] == ")":
            top = nums.pop()
            while top != '(':
                pfixlist.append(top)
                top = nums.pop()
        else:
            pfixlist.append(tokens[i])
    while not nums.is_empty():
        pfixlist.append(nums.pop())
    return " ".join(pfixlist)



def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    tokens = input_str.split()
    nums = Stack(30)
    for item in reversed(tokens):
        if item not in "+ - * / ** << >>":
            nums.push(item)
        else:
            op1 = nums.pop()
            op2 = nums.pop()
            str = op1 + ' ' + op2 + ' ' + item
            nums.push(str)
    return nums.peek()



