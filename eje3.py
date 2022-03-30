dias = int(input("Ingrese el número de días: "))
anios = dias//365
meses = (dias%365)//30
semanas = (dias-(anios*365+meses*30))//7
dias2 = dias-(anios*365+meses*30+semanas*7)
print(dias,"equivalen a:",anios,"años,",meses,"meses,",semanas,"semanas y",dias2,"dias")