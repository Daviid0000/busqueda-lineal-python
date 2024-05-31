def busqueda_lineal(lista, x):
    i=0

    for z in lista:
        if z == x:
            print("Valor obtenido:", z)
            return i
        i=i+1
    return -1

lista = [1, 2, 3, 4, 5, -1]
x = 4
resultado = busqueda_lineal(lista, x)
print("El valor se encuentra en el indice:", resultado)