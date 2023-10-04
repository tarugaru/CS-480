# Tallulah Cook
# CS 480
# Calculator Application:
    # objective: implement a simple calculator that takes in user input (Strings)
# 10/2/23 - 
# calculator.py
operators =[]
postfix = []
expression = []

def parseExp():
    while len(expression)>0:
        element = expression.pop(0)
        if element.isdigit() or element == ".":
            getNumVal(element)
        elif element == "+" or "*":
            evalOp(element)
        print(postfix)
        print(operators)

def getNumVal(element):
    char = None
    if len(expression)>0:
        char = expression[0]
    while char != None:
        if char.isdigit() or char=="." or char=="^":
            element = element + char
            expression.pop(0)
            if len(expression)> 0:
                char = expression[0]
            else:
                char = None
        else:
            char = None
    postfix.append(element)
    
def evalOp(element):
    if len(operators) >0:
        prevOp = operators[len(operators)-1]
        if (prevOp == "*" or prevOp == "/") and (element == "+" or element == "-"):
            postfix.append(prevOp)
            operators.pop()
            operators.append(element)
    else:
        operators.append(element)
        
expr = input("Evaluate: ")
#get rid of spaces in user input
expr = expr.replace(" ","")
expression = list(expr)
print(expression)
parseExp()

