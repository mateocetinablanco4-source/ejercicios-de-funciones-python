# zona de codigos 


def toma_precio():
    precio = int(input("por favor,digite el precio del articulo:"))
    return precio

def cal_descuento(precio):
    desc = precio *0.10
    return desc

def precio_f(desc, precio):
    precio_final = precio - desc
    return precio_final

def imprimir_rslt(precio_final):
    print("con 10% de descuento,el precio del articulo es de", precio_final)

#codigo principal de python

precio = toma_precio()
desc = cal_descuento(precio)
precio_final = precio_f(desc, precio)
imprimir_rslt(precio_final)
