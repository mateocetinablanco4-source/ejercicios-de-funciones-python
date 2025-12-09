
#------zona de codigo
#---------------
def pedir_radio():
    radio = float(input("digite el radio del cono:"))
    return radio
def pedir_altura():
    altura = float(input("digite la altura del cono:"))
    return altura
def definir_pi():
    black = float (3.14)
    return black


def calcular_volumen(radio, altura , black):
    vol = 0.33 * black * (radio**2) * altura
    return vol

def imprimir_datos(radio, altura):
    mensaje = "el radio del cono es: " + radio
    mensaje = "la altura del cono es: " + altura

def imprimir_resultado(resultado_volumen):
    print("el volumen del cilindro es:" + str(resultado_volumen))


# CODIGO PRINCIPAL PYTHON


radio = pedir_radio()
altura = pedir_altura()
black = definir_pi()
vol = calcular_volumen(radio , altura, black=3.14)
resultado = imprimir_resultado(vol)

    