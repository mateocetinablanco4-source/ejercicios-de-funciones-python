# zona de codigo

def tomar_lomgitud():
    longitud = int(input("digite la longitud del rectangulo(centimetros):"))
    return longitud

def tomar_ancho():
    ancho = int(input("digite el ancho del rectangulo (centimetros):"))
    return ancho

def calcular_area(longitud, ancho):
    area = longitud * ancho
    return area

def imprimir_resultado(area):
    print ("el area del rectangulo es:", area)


#codigo principal de python

longitud = tomar_lomgitud()
ancho = tomar_ancho()
area = calcular_area(longitud, ancho)
imprimir_resultado(area)
 