def iva_de_producto(producto) :
    '''Lee un número por teclado que pida el precio de un producto (puede tener decimales) y calcule el precio final con IVA. '''
    
    iva = (producto * .16)
    
    return iva

print("Calcula el iva de un producto")

producto = float(input("Precio del producto: "))
resultado = iva_de_producto(producto)

print(f"IVA = {resultado}")