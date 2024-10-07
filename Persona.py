class Persona:
    _contador_personas:int = 0

    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento

        Persona._contador_personas += 1

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre_setter):
        self._nombre = nombre_setter

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido_setter):
        self._apellido = apellido_setter

    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_nacimiento_setter):
        self._fecha_de_nacimiento = fecha_nacimiento_setter

    def presentarse(self):
        return f"Hola, mi nombre es {self._nombre} {self._apellido} y nací el {self._fecha_de_nacimiento}"

    @classmethod
    def cantidad_personas(cls)->int:
        return cls._contador_personas
