
#zona de codigo es python



def definir_altura():
    alt = 12
    return alt
def definir_base():
    base = 15
    return base
def calcular_area(base , altura):
    area = (base * altura) / 2
    return area

def imprimir_datos (base , altura):

    mensaje = "la base es" + base

    mensaje = "la altura es " + altura


    def imprimir_resultados (resultado_area):

        print("el area del triangulo es: " + str(resultado_area))




#codigo principal python

base= definir_base()

altura = definir_altura()

area = calcular_area( base,  altura)

resultado = imprimir_datos(altura)





    
    