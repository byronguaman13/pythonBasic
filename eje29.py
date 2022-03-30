from operator import truediv


def imprimir(dic):
    for indice in dic:
        print("Producto:",indice,"Precio:",dic[indice])

dic = {}
dic["pan"]=.12
dic["queso"]=2
total = 0
menu = True
while menu:
    op = int(input("Elija una opcion\n1.-Agregar producto\n2.-Facturar\n3.-Salir\n"))
    if op==1:
        indice = input("Ingrese el indice: ")
        valor = float(input("Ingrese el valor: "))
        dic[indice]=valor
        print(dic)
    elif op==2:
        fatura = True
        while fatura:
            imprimir(dic)
            print("Elija una opcion\n1.-Agregar a factura\n2.-Finalizar")
            opf = int(input())
            if opf==1:
                indice = input("Ingrese el producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                if dic.get(indice) is None:
                    print("Producto no encontrado")
                else:
                    total += float(dic.get(indice))*cantidad
                    print("El total es:",total)
            else:
                fatura=False
                total=0
    elif op==3:
        menu = False
    else:
        print("Ingrese una opcion valida")