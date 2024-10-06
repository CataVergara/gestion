class Asignatura:
    _contador_asignaturas:int = 0

    def __init__(self, nombre:str, codigo:str, creditos:int):
        self._nombre = nombre
        self._codigo = codigo
        self._creditos = creditos
        
        Asignatura._contador_asignaturas += 1

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, valor):
        self._creditos = valor

    # Métodos
    def mostrar_informacion(self):
        print(f"Asignatura: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}")

    @classmethod
    def cantidad_de_asignaturas(cls)->int:
        return cls._contador_asignaturas
