from Grupo import Grupo

class ProgramaAcademico:
    _contador_programas:int = 0

    def __init__(self, nombre:str, codigo:str):
        self._nombre = nombre
        self._codigo = codigo
        self._grupos = []  

        ProgramaAcademico._contador_programas += 1

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
    def grupos(self):
        return self._grupos

    def agregar_grupo(self, grupo):
        if grupo not in self._grupos:
            self._grupos.append(grupo)
        else:
            print(f"El grupo {grupo.numero_grupo} ya está incluido en el programa académico.")

    def eliminar_grupo(self, numero_grupo:int):
        grupo_a_eliminar = None
        for grupo in self._grupos:
            if grupo.numero_grupo == numero_grupo:
                grupo_a_eliminar = grupo
                break

        if grupo_a_eliminar:
            self._grupos.remove(grupo_a_eliminar)
        else:
            print(f"No se encontró un grupo con el número {numero_grupo} en el programa académico.")

    def mostrar_programa(self):
        print(f"Programa Académico: {self.nombre} (Código: {self.codigo})")
        if self._grupos:
            print("Grupos asignados:")
            for grupo in self._grupos:
                grupo.mostrar_grupo()  
        else:
            print("No hay grupos asignados a este programa académico.")

    @classmethod
    def cantidad_programas(cls)->int:
        return cls._contador_programas
