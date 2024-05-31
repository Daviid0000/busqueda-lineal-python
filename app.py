import time
inicio = time.time()

def busqueda_lineal(lista, x):
    i=0

    for z in lista:
        if z == x:
            print("Valor obtenido:", z)
            return i
        print(f"Valor no obtenido: {z}")
        i=i+1
    return -1

lista = [1, 6, 5, 4, 5, -1]
x = 5
resultado = busqueda_lineal(lista, x)
if lista[resultado] == x:
    print(f"El valor se encuentra en el indice: {resultado}")
elif lista[resultado] != x:
    print( "El valor no se encuentra en el lista")

fin = time.time()
print(f"Tiempo de ejecución: {fin-inicio}")