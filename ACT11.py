def quick_sort(lista):
    if len(lista) <= 1:
        return lista


    pivote = lista[0]
    menores = [x for x in lista[1:] if x<pivote]
    iguales = [x for x in lista if x==pivote]
    mayores = [x for x in lista[1:] if x>pivote]

    return quick_sort(menores)+iguales+quick_sort(mayores)

print("ORDENAMIENTOS DE DATOS")
lista = []
cantidad = int(input("CANTIDAD DE NOMBRES A INGRESAR: "))
contador = 1

while contador <= cantidad:
    elemento=input("INGRESO DE NOMBRE: ")
    lista.append(elemento)
    contador += 1


resultado = quick_sort(lista)
print(resultado)