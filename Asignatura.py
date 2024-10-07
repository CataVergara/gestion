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
    def nombre(self, nombre_setter):
        self._nombre = nombre_setter

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo_setter):
        self._codigo = codigo_setter

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, creditos_setter):
        self._creditos = creditos_setter

    # Métodos
    def mostrar_informacion(self):
        print(f"Asignatura: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}")

    @classmethod
    def cantidad_de_asignaturas(cls)->int:
        return cls._contador_asignaturas
