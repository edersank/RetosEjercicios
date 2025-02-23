from math import pow, pi
def area_circulo(radio) :
    '''Haz una aplicación que calcule el área de un círculo(pi*R2). El radio se pedirá por teclado '''
    PI = pi
    radio = float(radio)
    cuadradroNumero = pow(radio, 2)
    area = (pi * cuadradroNumero) 
    
    return area

print("Calcula el area de un circulo")
radio = input("Ingresa el radio: ")

resultado = area_circulo(radio)
print(f"El area es: {resultado}")