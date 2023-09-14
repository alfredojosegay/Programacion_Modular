def suma(a, b):
    
    return a + b

def resta(a, b):

    return a - b

def multiplicacion(a, b):

    return a * b

def division(a, b):

    return a / b

while True:
    print("Que operación desea realizar?: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = suma(a,b)
        print(f"El resultado de la suma es de: {resultado}")
    elif opcion == "2":
        c = float(input("Ingrese el primer número: "))
        d = float(input("Ingrese el segundo número: "))
        resultado = resta(c,d)
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
        e = float(input("Ingrese el primer número: "))
        f = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(e,f)
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        g = float(input("Ingrese el primer numero: "))
        h = float(input("Ingrese el segundo numero: "))
        resultado = division(g,h)
        print(f"El resultado de la división es: {resultado}")
    elif opcion == "5":
        print("¡Cerrando programa!")
        break
    