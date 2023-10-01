## operadores aritmeticos
x = 5
y = 6

#Suma
print(x+y)

#Resta
print(x-y)

#Producto
print(x*y)

#Division
print(x/y)

#Modulo
print(x%y)

#potencia
print(2**2)
print(x**2)
print(y**2)

#floor division
print(4//2)
print(x//y)
#Operadores de Asignacion
x = 30
x += 32
x -= 2
x *= 2
x /= 2
x %= 2
print(x)

#Operadores Logicos De Comparacion
a = 3
b = 2

# Igual
print( a == b)

#Diferente
print( a != b)

#Mayor que
print( a > b)

#Menor que
print( a < b)

#Mayor igual
print( a >= b)

#Menor igual
print( a <= b)


#Operadores Logicos
promedio = 100
asistencia = True
aprobado = (promedio > 70 )and asistencia
#and, or, not
print(aprobado )

#Operadores Identidad
j = "Hola"
k = "Hola "



#print(j is k.replace())
print(j is not k)

#Operadores de Pertenencia
print("a" in "Hola")
print("a" not in "Hola")

#lista
frutas = ["Manza", "Plaatano", "Sandia"]
print(frutas)



##Listas, tuple , set , dictonary

#Tuple: es una coleccion la cual esta ordenada y no es modificable. permite duplicados


#set: Es una coleccion la cual no esta ordenada y no es modificable no inexada. No permite duplicado


#Dictonary: Es una coleccion la cual esta ordenada es modificable. No permite duplicados

#lista
lista1 = tupla1 = ["🐯", "👽 ", " 🦁"]
lista1.insert(3,"🙊")
lista1 [2] = "🦓"
print(lista1)

#tupla
tupla1 = ("🐯", "👽 ", " 🦁")
print(tupla1)

#set
set1 = {"🐯", "👽 ", " 🦁"}
set1.add("🦅")
set1.add("🐺")
set1.add("🦝")
print(set1)

#diccionario
diccionario1 = {
    "tigre": "🐯",
    "los estraterrestres": "👽",
    "leon": "🦁"
}
diccionario1["mapache"] = "🦝"
diccionario1["lobo"] = "🐺"
print(diccionario1["lobo"])
print(diccionario1)

##crear una lista : 1, 2, 5, 3, 2, 3,3, 6, 10, 8, 9
#1. convertir la lista en un set para eliminar duplicados
#2.calcular la suma de los numeros usando una lista
#3.calcular la suma de los numeros usando un set
#4.crear un diccionario para almacenar las estadisticas
#numeros unicoas, suma total lista, suma total set
#maximo valor, minimo valor
#4.imprimir las estadisticas

# Crear la lista
numeros = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]

# Convertir la lista en un set para eliminar duplicados
numerosSet = set(numeros)

# Calcular la suma de los números usando una lista
sumaLista = sum(numeros)

# Calcular la suma de los números usando un set
sumaSet = sum(numerosSet)

# Encontrar el máximo valor
maximoValor = max(numeros)

# Encontrar el mínimo valor
minimoValor = min(numeros)

# Crear un diccionario para almacenar las estadísticas
estadisticas = {
    "NumerosUnicos": len(numerosSet),
    "SumaTotalLista": sumaLista,
    "SumaTotalSet": sumaSet,
    "MaximoValor": maximoValor,
    "MinimoValor": minimoValor
}

# Imprimir las estadísticas
for clave, valor in estadisticas.items():
    print(f"{clave}: {valor}")




#ciclo while
quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron  <= 3:
    vecesRegresaron += 1
    print("Han vuelto " + str (vecesRegresaron) + " veces")


#break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("error")


#continue
i = 0
while  i < 6:
    i += 1
    if i == 3:
        continue
        print(i)

#ciclo for for each
frutas = ["🍑", "🍊", "🍉"]

#for por cada
buscar = True
if buscar:
    for frutas in frutas:
        if frutas == " 🍑":
            print("Se encontro: " + frutas)
    else:
        print("Not Found")

