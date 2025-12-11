#zona de codigos

def toma_kilometros():
    kilometros = float(input("digite la cantidad de kilometros que desea convertir a millas:"))
    return kilometros

def calcular_millas(kilometros):
    millas = kilometros / 1.609
    return millas

def imprimir_rslt(millas):
    print("la cantidad de kilometros que inserto se traduce a", millas, "millas.")


#codigo principal de python
kilometros = toma_kilometros()
millas = calcular_millas(kilometros)
imprimir_rslt(millas)

