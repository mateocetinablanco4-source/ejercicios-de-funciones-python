#zona de codigos

def dia_cuenta():
    dinero = float(input("digite la cantidad de dinero que hay en su cuenta:"))
    return dinero
def calc_interes(dinero):
    interes = dinero * 0.05
    return interes
def total(dinero, interes):
    tot = dinero + interes
    return tot
def imprimir_rslt(interes,tot):
    print("el interes de su cuenta es de:", interes)
    print("el total en la cuenta despues de agregar el interes es de:", tot)

#codigo principal de python
dinero = dia_cuenta()
interes = calc_interes(dinero)
tot = total(dinero, interes)
imprimir_rslt(interes, tot)
