def bienvenida() :
    '''Declara un String que contenga tu nombre, después muestra un mensaje de bienvenida por consola. 
    Por ejemplo: si introduzco «Fernando», me aparezca «Bienvenido Fernando».'''
    nombre = input("Ingresa tu nombre: ")
    
    print(f"Bienvenido {nombre}")
    return nombre

bienvenida()