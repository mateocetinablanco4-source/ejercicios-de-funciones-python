#zona de codigos python


def solicitar_numero():
    numero = int(input("Ingrese un número: "))
    return numero

def determinar_par_impar(numero):
    if numero % 2 == 0:
        resultado = "par"
    else:
        resultado = "impar"
    return resultado

def imprimir_resultado(numero, resultado):

    print("El número " + str(numero) + " es " + resultado)

#codigo princiál de python

numero = solicitar_numero()

resultado = determinar_par_impar(numero)

imprimir_resultado(numero, resultado)