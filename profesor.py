from Persona import Persona
<<<<<<< Updated upstream


class Profesor(Persona):
    
    contador_profesores = 0

    def __init__(self, nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento):
        
        super().__init__(nombre, apellido, fecha_de_nacimiento)

        self._numero_empleado = numero_empleado
        self._departamento = departamento

        
        Profesor.contador_profesores += 1

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, valor):
        self._numero_empleado = valor

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, valor):
        self._departamento = valor

   
    def ensenar(self, materia):
        print(f"El profesor {self.nombre} {self.apellido} enseña la materia: {materia}.")

    
    def presentarse(self):
        return f"Hola, soy el profesor {self.nombre} {self.apellido}, con número de empleado {self.numero_empleado}, del departamento de {self.departamento}."

    @staticmethod
    def cantidad_profesores():
        return Profesor.contador_profesores
=======

class Profesor(Persona):
    def __init__(self, contador_profesores:int, numero_empleado:str, departamento:str):
        self._contador_profesores = contador_profesores
        self.__numero_empleado = numero_empleado
        self.__departamento = departamento

    @property
    def numero_empleado(self):
        return self.__numero_empleado
    
    @numero_empleado.setter
    def numero_empleado(self, numero_empleado_setter):
        self.__numero_empleado = numero_empleado_setter

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento_setter):
        self.__departamento = departamento_setter

    def cantidad_profesores(self, cantidad_profesores:int):
        pass

    def enseñar(self, materia:str):
        pass

    def presentarse(self):
        pass
>>>>>>> Stashed changes
