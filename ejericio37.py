# zona de codigos python

def solicitar_primer_numero():
    num1 = int(input("digite el primer numero:"))
    return num1

def solicitar_segunda_numero():
    num2 = int(input("digite el segundo numero:"))
    return num2

def  verificar_multiplo(num1, num2):
     if num1 % num2 == 0:
            resultado = "es multiplo"
     else:
         resultado = "no es multiplo"
         return resultado
     
def imprimir_datos(num1, num2, resultado):
     
     print(" el primer numero es :"+ str(num1))
     print("el segundo numero es : "+str(num2))

def imprimir_resultado(num1, num2, resultado):
    print(str (num1) + ""+ resultado +" de " +str (num2))

    #codigo principal de python

    num1 = solicitar_primer_numero()

    num2 = solicitar_segunda_numero()

    imprimir_datos(num1, num2)

    resultado = verificar_multiplo(num1, num2)

    imprimir_resultado(num1, num2, resultado)
