'''Reemplaza todas las a del String anterior por una e'''
def cambia_por_e(frase):
    frase_dos = ""

    for letra in frase:
        if letra == "a":
            letra = "e"
            
        frase_dos += letra
        
    print(frase_dos)

frase = "La lluvia en Sevilla es una maravilla"

# frase_nueva = frase.replace("a", "e")

# #print(frase_nueva)

cambia_por_e(frase)


