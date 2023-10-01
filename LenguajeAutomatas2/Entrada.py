# ENTRADA DE DATOS
"""
print("Ingresa tu nombre:")
nombre = input()
print(type(nombre))
palabras = nombre.split(" ")
nombre = nombre.capitalize()
nombre = nombre.replace(" ", " ")

for palabra in palabras:
    print(palabra.capitalize())
print("Hola " + nombre)
"""
print("Ingresa nombre:")
nombre = input()
palabras = nombre.split(" ")
nombreCapitalizado = ""

for palabra in palabras:
    nombreCapitalizado += palabra.capitalize() + " "

print(nombreCapitalizado)