def  definir_ancho():
    anc = 16
    return anc
def definir_longitud():
    longitud = 20
    return longitud
def calcular_area(ancho, longitud):
    area = (ancho * longitud)
    return area

def imprimir_datos( ancho , longitud):
    mensaje = "el ancho es:" + ancho

    mensaje = "la longitud es:" + longitud


def imprimir_resultado ( resultado_area ):

    print ("el area del rfectangulo es:"+ str(resultado_area))


#codigo principal es python

    ancho = definir_ancho()

    longitud = definir_longitud()

    area = calcular_area(ancho , longitud)

    resultado = imprimir_resultado(area)
    
