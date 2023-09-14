def buscar_numero(arreglo, numero):
    
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            return i
    return -1

arreglo = [12, 34, 56, 78, 90, 123, 45, 67]

numero_a_buscar = int(input("Ingrese el número que desea buscar: "))

posicion = buscar_numero(arreglo, numero_a_buscar)

if posicion != -1:
    print(f"El número {numero_a_buscar} se encuentra en la posición {posicion} del arreglo.")
else:
    print(f"El número {numero_a_buscar} no se encuentra en el arreglo.")