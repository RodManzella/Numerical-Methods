
def bissection(equation, interval):

    return 0

def falsePosition(equation, interval):

    return 0


def mil (equation, interval):

    return 0

def newtonRaphson(equation, interval):

    return 0

def hasRoot(equation, interval):

    if 'x' or 'X' in equation:
        equation = equation.Lower()
        funcValueA = int(equation.replace('x', interval[0]))
        funcValueB = int(equation.replace('x', interval[1]))
    
    if (funcValueA >= 0 and funcValueB) < 0 or (funcValueA < 0 and funcValueB >= 0):
        return True
    
    return False

             

    return 0
