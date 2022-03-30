from random import randint

def ppt(op):
    if op==1:
        r="piedra"
    elif op ==2:
        r= "papel"
    elif op ==3:
        r= "tijera"
    return r

ganadas = 0
ganadasMaquina=0
while ganadas<3 and ganadasMaquina<3:
    opUsuario = int(input("Ingres una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijera\n"))
    if opUsuario>3 or opUsuario<1:
        print("Ingrese una opcion valida")
        continue
    opMaquina = randint(1,3)
    print("El usuario eligio: ",ppt(opUsuario))
    print("La maquina eligio: ",ppt(opMaquina))
    if (opUsuario==1 and opMaquina==3) or (opUsuario==2 and opMaquina==1) or (opUsuario==3 and opMaquina==2):
        print("Gana el usuario")
        ganadas+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        print("Gana la maquina")
        ganadasMaquina+=1
    print("Ganadas usuario:",ganadas)
    print("Ganadas maquina:",ganadasMaquina,"\n")

    