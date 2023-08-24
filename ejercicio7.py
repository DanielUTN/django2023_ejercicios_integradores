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

#----------------0--------------------------
#CLASE CUENTA
class Cuenta():

    def __init__(self, titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    #getters
    @property
    def cantidad(self):
        return self._cantidad


    #setter
    @cantidad.setter
    def cantidad(self,value):
        try:
            float(value)
            self._cantidad = value
        except ValueError:
            raise TypeError('Ingrese cantidad valida')

    def mostrar(self):
        print(f'La cuenta pertenece a: {self.titular.nombre}, Edad:{self.titular.edad}, DNI:{self.titular.dni}, Cantidad:{self.cantidad}')

    def ingresar(self,monto):
        if monto > 0:
            self.cantidad = self.cantidad + monto
        else:
            self.monto = 0

    def retirar(self, monto):
        self.cantidad = self.cantidad-monto

print("\033[H\033[J") #limpiar consola

# alumno = Persona('Jose',25,3456879)
alumnoCuenta = Cuenta(Persona('Jose',25,3456879),1000)
alumnoCuenta.mostrar()

print('prueba de ingresar----------------------------')
alumnoCuenta.ingresar(3000)
print('Nuevo Monto luego de ingresar:',alumnoCuenta.cantidad)

print('\n')
print('prueba de retirar----------------------------')
alumnoCuenta.retirar(1500)
print('Monto luego del retirar:',alumnoCuenta.cantidad)




