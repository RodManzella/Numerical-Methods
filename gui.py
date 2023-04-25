import numericalMethods as method
import math

def func(x):
    return math.pow(x, 2) - math.exp(x);

def gerador(x):
    return -math.sqrt(math.exp(x))

def derivada(x):
    h = 0.01
    return (func(x + h) - func(x)) / h



















