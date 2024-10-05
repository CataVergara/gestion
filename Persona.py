class Persona:
    
    contador_personas = 0

<<<<<<< Updated upstream
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_de_nacimiento = fecha_de_nacimiento

        
        Persona.contador_personas += 1

    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, valor):
        self._fecha_de_nacimiento = valor

    
    def presentarse(self):
        print(f"Hola, mi nombre es {self._nombre} {self._apellido}. Nací el {self._fecha_de_nacimiento}.")

    
    @staticmethod
    def cantidad_personas():
        return Persona.contador_personas
=======
    # Getter del atributo nombre
    @property
    def nombre(self):
        return self.__nombre
    
    # Setter del atributo nombre
    @nombre.setter
    def nombre(self, nombre_setter):
        self.__nombre = nombre_setter

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido_setter):
        self.__apellido = apellido_setter

    @property
    def fecha_de_nacimiento(self):
        return self.__fecha_de_nacimiento
    
    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, fecha_nacimiento_setter):
        self.__fecha_de_nacimiento = fecha_nacimiento_setter
    
    def cantidad_personas(self, cantidad_personas:int):
        for persona in cantidad_personas:
            return persona

    def presentarse(self):
        print("Hola, mi nombre es " + self.nombre)
>>>>>>> Stashed changes
