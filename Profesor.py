from Persona import Persona

class Profesor(Persona):
    _contador_profesores:int = 0

    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str, numero_empleado:str, departamento:str):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._numero_empleado = numero_empleado
        self._departamento = departamento

        Profesor._contador_profesores += 1

    @property
    def numero_empleado(self):
        return self._numero_empleado

    @numero_empleado.setter
    def numero_empleado(self, numero_empleado_setter):
        self._numero_empleado = numero_empleado_setter

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento_setter):
        self._departamento = departamento_setter

    def ensenar(self, materia:str):
        print(f"El profesor {self.nombre} {self.apellido} enseña la materia: {materia}.")

    # Heredado de la clase persona
    def presentarse(self):
        return f"{super().presentarse()}. Con número de empleado {self.numero_empleado}, del departamento de {self.departamento}."

    @classmethod
    def cantidad_profesores(cls)->int:
        return cls._contador_profesores
