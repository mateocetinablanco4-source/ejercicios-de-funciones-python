#zona de codigo

def toma_hora():
    horas = int(input("digite el numero de horas que quiere convertir en minutos:"))
    return horas

def calc_mins(horas):
    mins = horas * 60
    return mins 

def calc_mins(horas):
    mins = horas * 60
    return mins

def imprimir_rslt(mins):
    print("las cantidad de horas que introdujo,se traducen a:", mins, "minutos.")

# codigo principal de python

horas = toma_hora()
mins = calc_mins(horas)
imprimir_rslt(mins)
