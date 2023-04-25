import math
import gui as f



def bissection(a, b, limit):

    if f.func(a) * f.func(b) < 0:

        while math.fabs(b-a) / 2 > limit:
            cut = (a + b) / 2

            if f.func(cut) == 0:
                break
            else:
                if f.func(a) * f.func(cut):
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
   x0 = (a * f.func(b) - b * f.func(a)) / f.func(b) - f.func(a)

   while c > limit or math.fabs(f.func(x0)):
       
        if f.func(a) * f.func(x0) < 0:
           b = x0
        else:
           a = x0


        c = b - a
        x0 = (a * f.func(b) - b * f.func(a)) / f.func(b) - f.func(a)
        count = count + 1

        if count >= iteration:
            break


def newtonRaphson(aproxInit, limit):

    iterations = 100
    i = 1

    while math.fabs(f.func(aproxInit)):

        x = aproxInit - f.func(aproxInit) / f.derivada(aproxInit)
        aproxInit = x
        i = i + 1

        if(i >= iterations):
            print("Raiz não foi encontrada")
    
    if(i < iterations):
        print(f"Raiz é :{aproxInit}")



       


