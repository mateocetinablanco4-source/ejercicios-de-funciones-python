
#zona de codigos python


def definir_radio():
    radio = 10
    return radio

def definir_pi():
    pi = 3.14
    return pi

def calcular_area(pi, radio):
    area = pi * (radio **2 )
    return area
def imprimir_datos(pi, radio):
    mensaje = "El resultado de pi es : " + pi
    mensaje = "El radio del circulo es : " + radio
    
def imprimir_resultado(resultado_area):
    print ("El area del circulo es: "+ str(resultado_area))



#codigo principal es python 

 
radio = definir_radio()

pi = definir_pi()

area = calcular_area(pi, radio)

resultado = imprimir_resultado(area)