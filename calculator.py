# Tallulah Cook
# CS 480
# Calculator Application:
    # objective: implement a simple calculator that takes in user input (Strings)
# 10/2/23 - 
# calculator.py
def evaluate(expr):
    #shunting yard algorithm-- need a stack [operators] and queue[postfix]
    operators = []
    postfix = []
    while len(expr)>0:
        element = expr.pop(0)
        if element.isdigit() and len(expr)>0:
            char = expr[0]
            while char.isdigit():
                element = element + char
                expr.pop(0)
                char = expr[0]
            postfix.append(element)
        elif element.isdigit():
            postfix.append(element)
        else:
            #if it is not a digit, but not a ')' first look at the stack to see if a higher
            #precedence operation takes place. if it is a ')' add in all operators until '('
            #maybe a good place for bracket/parenthesis error checking?
            operators.append(element)
    print(postfix)
    print(operators)
    #after all checking is added, should end up with an empty operators stack, 
    #and a full queue
    
        
    
expression = input("Evaluate: ")
#get rid of spaces in user input
expression = expression.replace(" ","")
expr = []
expr = list(expression)
print(expr)
evaluate(expr)
