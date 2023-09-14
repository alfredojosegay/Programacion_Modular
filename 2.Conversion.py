
def celsius_a_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f" Los {celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")

fahrenheit = float(input("Ingrese la temperatura en grados fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print(f" Los {fahrenheit} Los grados Fahrenheit son equivalentes a {celsius} grados Celsius.")