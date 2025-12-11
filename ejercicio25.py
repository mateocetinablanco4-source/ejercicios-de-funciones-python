#zona de codigos python

def pedir_num1():
    num1 = float (input("Digite primer numero"))
    return num1

def pedir_num2():
    num2 = float (input ("Digite segundo numero"))
    return num2

def calcular_numeros(num1, num2):
    div = num1 / num2
    return div

def imprimir_resultado(div):

    print("La division de los 2 numeros es: "+ str(div))


#codigo principal de pýthon

num1 = pedir_num1()

num2 = pedir_num2()

div = calcular_numeros(num1, num2)

resultado = imprimir_resultado(div)