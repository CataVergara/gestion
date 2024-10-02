class Persona:
    def __init__(self, contador_personas:int, nombre:str, apellido: str, fecha_de_nacimiento:str):
        self._contador_personas = contador_personas
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_de_nacimiento = fecha_de_nacimiento


    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre_setter):
        self.__nombre = nombre_setter
    def cantidad_personas():
        pass

    def presentarse(self, materia:str):
        pass

    def presentarse():
        pass