def convetir_numero_vs_caracter(numero) :
    numero = int(numero)
    caracter = chr(numero)
    
    return  caracter


print("Ingresa el numero que quieres convertir a Ascii")
numero = input("Ingresa numero: ")

resultado = convetir_numero_vs_caracter(numero)
print(f"{numero} = {resultado}")