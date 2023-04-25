import numericalMethods as method
import math

def func(x):
    return math.pow(x, 2) - math.exp(x);

def gerador(x):
    return -math.sqrt(math.exp(x))

def derivada(x):
    h = 0.01
    return (math.pow(x, 2) - math.exp(x)) / h


flag = True

while flag:
    print(f"Digite 1 para aproximar raiz por bissecção: ")
    print(f"Digite 2 para aproximar raiz por falsa-posição: ")
    print(f"Digite 3 para aproximar raiz por NewTon-Raphson: ")
    print(f"Digite 4 para aproximar raiz por Iteração Linear: ")
    print("QUALQUER TECLA - SAIR")

    escolha = int(input("Digite:"))

    if escolha == 1:
        a = float(input("Digite valor de limite inicial (a): "))
        b = float(input("Digite o valor de limite final (b): "))
        limite = float(input("Digite o erro: "))

        method.bissection(a, b , limite)
        

    elif escolha  == 2:
        a = float(input("Digite valor de limite inicial (a): "))
        b = float(input("Digite o valor de limite final (b): "))
        limite = float(input("Digite o erro: "))

        method.fakePos(a ,b , limite)

    elif escolha  == 3:
        chuteInicial = float(input("Digite o chute inicial: "))
        limite = float(input("Digite o erro: "))

        method.newtonRaphson(chuteInicial, limite)
    
    elif escolha  == 4:
        chuteInicial = float(input("Digite o chute inicial: "))
        limite = float(input("Digite o erro: "))

        method.fixedPoint(chuteInicial, limite)

    else:
        flag = False

print("Acabou: ")


        

        




















