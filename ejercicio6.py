class Persona:

    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def constructor(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # getters for each attribute - Regla primero los getters siempre
    @property  # decorator to make the method a property of this class
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni

    # setters for each attribute
    @nombre.setter
    def nombre(self, value):
        # print('Setting Nombre')
        try:
            str(value)
            self._nombre = value
        except ValueError:
            raise TypeError('Ingrese un nombre valido')

    @edad.setter
    def edad(self, value):
        # print('Cambiando Edad')
        try:
            int(value)
            self._edad = value
        except ValueError:
            raise TypeError('Ingresa edad valida')

    @dni.setter
    def dni(self, value):
        # print('Cambiando DNI')
        try:
            int(value)
            self._dni = value
        except ValueError:
            raise TypeError('Ingresa un DNI valido')

    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self.edad > 18


print("\033[H\033[J") #limpiar consola

alumno = Persona('jorge', 23, 564)
alumno.mostrar()
print('\n')
print('\n')

print(alumno.es_mayor_de_edad())
print('\n')
print('\n')
print(alumno.nombre)



