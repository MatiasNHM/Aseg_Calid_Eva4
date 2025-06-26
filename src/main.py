#Ejemplos
def sumar(a,b):
    return a+b


#Validacion de fecha
def ValFecha(mes, dia):
    if type(mes) == int and type(dia) == int:
        if (1 <= mes <= 12):
            if (1 <= dia <= 31):
                fecha = mes*100 + dia
                return fecha >= 625
            return False
        return False
    return False
        

dominio = ["gmail.com","yahoo.com","hotmail.com"]  
def ValCorreo(correo):

    if type(correo) != str:
        return False
    
    partes = correo.split("@")
    if len(partes) != 2:
        return False
    
    if partes[1] not in dominio:
        return False
    
    return type(correo) == str and len(correo.split("@")) == 2 and partes[1] in dominio


def ValContrasena(contrasena):

    if type(contrasena) != str:
        return False
    
    cantidad = len(contrasena)
    if cantidad < 12 or cantidad > 30:
        return False

    mayus = False
    minus = False
    numer = False

    for i in range(len(contrasena)):
        if contrasena[i].isnumeric():
            numer = True
        if contrasena[i].isupper():
            mayus = True
        if contrasena[i].islower():
            minus = True
    if numer and mayus and minus:
        return True
    else:
        return False
        



