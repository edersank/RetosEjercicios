def mayor_dos_numeros(x, y) :
    x = int(x)
    y = int(y)
    resultado = 0
    
    if x != y :
        if x > y:
            resultado = x
        else :
            resultado = y
    else :
        resultado = "Ambos numeros son iguales"
        
    return resultado

print("Ingresa dos numeros:")
x = input("Primer numero: ")
y = input("Segundo numero: ")

resultado = mayor_dos_numeros(x, y)
print(f"El número mayor es: {resultado}")