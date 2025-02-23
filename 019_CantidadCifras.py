'''Pide por teclado un número entero positivo (debemos controlarlo) y muestra  el número de cifras que tiene. 
Por ejemplo: si introducimos 1250, nos muestre que tiene 4 cifras. Tendremos que controlar si tiene una o mas cifras, al mostrar el mensaje.'''

#Funcion para mostrar la cantidad de cifras
        
def valida_numero(numero):
    isnumber = numero.isdigit()
    return isnumber
    
def cuenta_digitos(isnumber, numero):
    
    if isnumber:
        longitud = len(numero)
        print(f"El numero {numero}, tiene {longitud} cifras")
    else:
        print("No es una cifra numerica")

#ingresar numero
numero = input("Ingresa un numero: ")

validar_numero = valida_numero(numero)
resultado = cuenta_digitos(validar_numero, numero)