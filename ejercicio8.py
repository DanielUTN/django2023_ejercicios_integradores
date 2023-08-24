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

#-------------clase cuenta Joven
class CuentaJoven (Cuenta):

    def __init__(self, titular, cantidad,bonificacion):
        super().__init__(titular,cantidad)
        self.bonificacion = bonificacion

    #getter
    @property
    def bonificacion(self):
        return self._bonificacion

    #setter
    @bonificacion.setter
    def bonificacion(self, value):
        self._bonificacion = value

    def es_Titular_Valido(self):
        return (self.titular.edad > 18 and self.titular.edad < 25)

    def retirar(self, monto):
        if (self.es_Titular_Valido() and monto > 0):
            super().retirar(monto)
        elif self.es_Titular_Valido()==False:
            print('El titular no es valido para realizar la operacion')

    def mostrar(self):
        print(f"Cuenta Joven pertenieciente a: {self.titular.nombre}, Edad: {self.titular.edad}, DNI: {self.titular.dni} \n")
        print(f"Bonificacion: {self.bonificacion}")

print("\033[H\033[J") #limpiar consola

cliente= Persona('Capusoto',24,57543364)

cuentaJoven = CuentaJoven(cliente,8000,5000)

print('Prueba si es valido-------------')
print(cuentaJoven.es_Titular_Valido())
print('\n')
print('\n')

print('PRUEBA DE RETIRAR-----------------')
cuentaJoven.retirar(900)
print(cuentaJoven.cantidad)




print('\n')
print('\n')
print('PRUEBA DE MOSTRAR--------------------------')
print('\n')
cuentaJoven.mostrar()





