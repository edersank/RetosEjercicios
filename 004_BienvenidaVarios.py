def bienvenida(*args) :
    '''Modifica la aplicación anterior, para que nos pida los nombre que queremos introducir.
    recibira n cantidad de nombres'''
    
    for nombre in args :
        print(f"Bienvenido {nombre}")
    

bienvenida("Eder", "Gael", "Mateo", "Liam")