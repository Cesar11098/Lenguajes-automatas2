edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)





contador = 0
while contador < 5:
    print(contador)
    contador += 1



for i in range(10):
    if i == 3:
        continue  # Salta la iteración cuando i es igual a 3
    if i == 7:
        break  # Sale del bucle cuando i es igual a 7
    print(i)