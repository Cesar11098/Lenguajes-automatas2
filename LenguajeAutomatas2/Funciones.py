#Clases y Objetos
class Alumno:
    nombre  = " Emir "
    def __init__(self, nombre, numeroControl, edad):
        self.nombre = nombre
        self.numeroControl = numeroControl
        self.edad = edad


alumnoEmir = Alumno(nombre = "Emir ", numeroControl = "20232245", edad = 20)
alumnoAngel = Alumno(nombre = "Angel", numeroControl = "19230246", edad=22)
alumnoLess = Alumno(nombre="Less", numeroControl= "20230980", edad=20)


print(alumnoEmir.nombre)
print(alumnoAngel.nombre)
print(alumnoLess.nombre)
