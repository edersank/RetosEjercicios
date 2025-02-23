def calculadora_dos_numeros() :
    
    A = int(input("Ingresa A = "))
    B = int(input("Ingresa B = "))
    
    
    suma = A + B
    resta = A - B
    multiplicacion = A * B
    division = A / B
    modulo = A % B
    
    print(f"{A} + {B} = {suma}")
    print(f"{A} - {B} = {resta}")
    print(f"{A} * {B} = {multiplicacion}")
    print(f"{A} / {B} = {division}")
    print(f"{A} % {B} = {modulo}")
    
    
print("""Ingresa un valor para A y B, el programa te mostrara 
el resultada para cada operacion con estos numeros""")
print("")
calculadora_dos_numeros()