import math


def func(x):
    return math.pow(x, 2) - math.exp(x);

def gerador(x):
    return -math.sqrt(math.exp(x))

def derivada(x):
    h = 0.01
    return (math.pow(x, 2) - math.exp(x)) / h



def bissection(a, b, limit):

    if func(a) * func(b) < 0:

        while math.fabs(b-a) / 2 > limit:
            cut = (a + b) / 2

            if func(cut) == 0:
                break
            else:
                if func(a) * func(cut):
                    b = cut
                else:
                    a = cut
        
        print(f"Raiz é {cut}")
    
    else:
        print("Não há raiz nesse intervalo")




def fakePos(a, b, limit):
   
   count = 0
   iteration = 100
   c = b - a
   x0 = (a * func(b) - b * func(a)) / func(b) - func(a)

   while c > limit or math.fabs(f.func(x0)):
       
        if func(a) * func(x0) < 0:
           b = x0
        else:
           a = x0


        c = b - a
        x0 = (a * func(b) - b * func(a)) / func(b) - func(a)
        count = count + 1

        if count >= iteration:
            break


def newtonRaphson(aproxInit, limit):

    iterations = 100
    i = 1

    while math.fabs(func(aproxInit)) > limit:

        x = aproxInit - func(aproxInit) / derivada(aproxInit)
        aproxInit = x
        i = i + 1

        if(i >= iterations):
            print("Raiz não foi encontrada")
    
    if(i < iterations):
        print(f"Raiz é :{aproxInit}")


def fixedPoint(aproxInit, limit):
    iterations = 100
    i = 1
    count  = 0

    while math.fabs(func(aproxInit)) > limit:
        x1 = gerador(aproxInit)
        x0 = x1
        i = i + 1

        if i >= iterations:
            print("Raiz não foi encontrada")
            break

        count = count + 1

    if i < iterations:
        print(f"A raiz é {aproxInit}")
        print(count)


       


