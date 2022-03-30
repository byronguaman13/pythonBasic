a = 0
b = 0

print("La ecuacion es: "+str(a)+"x + "+str(b)+" = 0")

if a==b==0:
    r = "Todos los numeros son solucion"
elif a==0:
    r = "No existe solucion"
else:
    r = "La unica solucion es: " + str(-b/a)
print(r)