#zona de codigo

def pedir_pulgadas():
    pulg = float (input(" Digite cantidad de pulgadas que desea convertir:  "))
    return pulg

def convertir_pulg_cm(pulg):
    cm = pulg * 2.54
    return cm

def imprimir_datos(pulg):
    mensaje = "Las pulgadas que deseas convertir son: " + pulg

def imprimir_resul(pulg, cm):
    print (f"{pulg} pulgadas  equivalen a {cm} centimetros")


#codigo principal de python

pulg = pedir_pulgadas()
cm = convertir_pulg_cm(pulg)
resultado = imprimir_resul(pulg, cm)