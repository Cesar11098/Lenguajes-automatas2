# CLASES Y OBJETOS

# CREANDO LA CLASE
class Alumno:
    def _init_(self,numControl, nombre, edad):
        self.numControl = numControl
        self.nombre = nombre
        self.edad = edad

    def _str_(self):
        return f"({self.numControl}) {self.nombre} ({self.edad})"

# CREANDO EL OBJETO
alumnoEmir = Alumno("20232245", nombre = "Emir", edad = 20)
alumnoRoxel = Alumno("22230979", nombre = "Roxel", edad = 20)
alumnoVictor = Alumno ("22230979", nombre = "Victor", edad = 20)

print(alumnoVictor)
print(alumnoEmir)
print(alumnoRoxel)