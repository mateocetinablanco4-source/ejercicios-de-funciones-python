# zona codigos python

def prim_num():
    num1 = int(input("digite el primer numero:"))
    return num1
def seg_num():
    num2 = int(input("digite el segundo numero:"))
    return num2
def calc_prom(num1, num2):
    prom = (num1 + num2)/2
    return prom

def imprimir_resultado(prom):
    print("el promedio de ambos numeros es de:", prom)

#codigo principal de python

num1 = prim_num()

num2 = seg_num()

prom = calc_prom(num1, num2)

imprimir_resultado(prom)

   
    