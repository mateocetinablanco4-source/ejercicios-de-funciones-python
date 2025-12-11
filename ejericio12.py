#zona de codigos oython

def definir_lado():
    lado = 4
    return lado

def calcular_area(lado):
    area = lado * lado
    return area

def imprimir_datos():

    mensaje = "el lado del cuadrado es :" + definir_lado

def imprimir_result(resultado):

    print("El resultado del area es: "+ str(resultado))

#codigo principal de python


lado = definir_lado()

area = calcular_area(lado)

resultado = imprimir_result(area)