 #zona de codigos de python

def prim_num():
    num1 = int (input("digite el primer numero: "))
    return num1

def seg_num():
    num2 = int(input("digite el segundo numero:"))
    return num2

def menosmas (num1, num2):

    if num1 > num2:
        
        print("el primer numero es mayor que el segundo.")
    else:
        print("el segundo numero es mayor que el primero.")

def imprimir_rst():

    print ("el programa finalizo.")


#codigo principal de python

num1 = prim_num()

num2 = seg_num()

menosmas(num1, num2)

imprimir_rst() 