#zona de codigos python

def definir_base():
    base = 10
    return base

def definir_altura():
    altura = 4
    return altura

def calcular_area(base, altura):
    area = base * altura
    return area

def imprimir_datos(base, altura):

    mensaje = "la base del paralelogramo :" + base
    mensaje = "la altura del paralelogramo es :" + altura
    

def imprimir_result(resultado):

    print("El resultado del area es: "+ str(resultado))

#codigo de principal de python

base = definir_base()

altura = definir_altura()

area = calcular_area(base, altura)

resultado = imprimir_result(area)