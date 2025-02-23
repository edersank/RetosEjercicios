def convetir_caracter_vs_numero(caracter) :
    numero = ord(caracter) #convierte en su valor ascii el caracter
    
    return  numero


print("Ingresa el numero que quieres convertir a Ascii")
caracter = input("Ingresa un caracter: ")

resultado = convetir_caracter_vs_numero(caracter)
print(f"{caracter} = {resultado}")