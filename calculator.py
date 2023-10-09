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
    validExp = True
    if expression[0]=="-":
        getNumVal(expression.pop(0))
    while len(expression)>0 and validExp:
        element = expression.pop(0)
        if element.isdigit() or element == ".":
            getNumVal(element)
        elif element == "c":
            validExp = evalCos(element)
        elif element == "s":
            evalSin(element)
        elif element == "l":
            evalLog(element)
        elif element == "n":
            evalLn(element)
        elif element == "+" or "*" or "-":
            evalOp(element)
        print(postfix)
        print(operators)
        
def evalCos(element):
    validCos= True
    print("eval cos")
    if expression[0]=="(":
        expression.pop(0)
        #evaluate the inside of cos
        print("confirmed")
    else:
        validCos = False
        print("invalid cos")
    return validCos

def evalSin(element):
    validSin= True
    print("eval sin")
    if expression[0]=="(":
        expression.pop(0)
        #evaluate the inside of cos
        print("confirmed")
    else:
        validSin = False
        print("invalid cos")
    return validSin
    
def evalLog(element):
    validLog= True
    print("eval log")
    if expression[0]=="(":
        expression.pop(0)
        #evaluate the inside of cos
        print("confirmed")
    else:
        validLog = False
        print("invalid log")
    return validLog
    
def evalLn(element):
    validLn= True
    print("eval ln")
    if expression[0]=="(":
        expression.pop(0)
        #evaluate the inside of cos
        print("confirmed")
    else:
        validLn = False
        print("invalid log")
    return validLn
    
def getNumVal(element):
    char = None
    expFlag = bool(False)
    if len(expression)>0:
        char = expression[0]
    while char != None:
        if char.isdigit() or char=="." or char=="^":
            if char == "^":
                expFlag = bool(True)
            element = element + char
            expression.pop(0)
            if len(expression)> 0:
                char = expression[0]
            else:
                char = None
        else:
            char = None
    if expFlag:
        num =element.split("^")
        base = (float)(num[0])
        exp = (float)(num[1])
        element = base**exp
    element = (float)(element)
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
    if expression[0] == "-":
        getNumVal(expression.pop(0))
    
expr = input("Evaluate: ")
#get rid of spaces in user input
expr = expr.replace(" ","")
expr = expr.replace("sin", "s")
expr = expr.replace("cos","c")
expr = expr.replace("log", "l")
expr = expr.replace("ln", "n")
print(expr)
expression = list(expr)
print(expression)
parseExp()

