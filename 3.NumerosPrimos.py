def encontrar_numero_primo(numero):
    
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 7
    return True

def encontrar_primos_en_rango(inicial, final):

    print(f"Los números primos desde {inicial} a {final} son: ")
    for numero in range(inicial, final + 1):
        if encontrar_numero_primo(numero):
            print(numero)

inicial = int(input("Ingrese el primer numero: "))
final = int(input("Ingrese el número final: "))

encontrar_primos_en_rango(inicial, final)
