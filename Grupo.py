from Asignatura import Asignatura
from Profesor import Profesor
from Estudiante import Estudiante

class Grupo:
    _contador_grupos:int = 0

    def __init__(self, numero_grupo:int, asignatura:Asignatura, profesor:Profesor):
        self._numero_grupo = numero_grupo
        self._asignatura = asignatura
        self._profesor = profesor
        self._estudiantes = []

        Grupo._contador_grupos += 1

    @property
    def numero_grupo(self):
        return self._numero_grupo

    @numero_grupo.setter
    def numero_grupo(self, numero_grupo_setter):
        self._numero_grupo = numero_grupo_setter

    @property
    def asignatura(self):
        return self._asignatura

    @asignatura.setter
    def asignatura(self, asignatura_setter):
        self._asignatura = asignatura_setter

    @property
    def profesor(self):
        return self._profesor

    @profesor.setter
    def profesor(self, profesor_setter):
        self._profesor = profesor_setter

    @property
    def estudiantes(self):
        return self._estudiantes

    @estudiantes.setter
    def estudiantes(self, estudiantes_setter):
        self._estudiantes = estudiantes_setter

    def agregar_estudiante(self, estudiante:Estudiante):
        if estudiante not in self._estudiantes:
            self._estudiantes.append(estudiante)
            print(f"Estudiante {estudiante.nombre} agregado al grupo {self._numero_grupo}.")
        else:
            print(f"El estudiante {estudiante.nombre} ya está en el grupo {self._numero_grupo}.")

    def eliminar_estudiante(self, matricula:str):
        for estudiante in self._estudiantes:
            if estudiante.matricula == matricula:
                self._estudiantes.remove(estudiante)
                print(f"Estudiante con matrícula {matricula} eliminado del grupo {self._numero_grupo}.")
                return
        print(f"No se encontró un estudiante con la matrícula {matricula} en el grupo {self._numero_grupo}.")

    def mostrar_grupo(self):
        print(f"Grupo {self._numero_grupo} - Asignatura: {self._asignatura.nombre} - Profesor: {self._profesor.nombre}")
        print("Estudiantes en el grupo:")
        for estudiante in self._estudiantes:
            print(f"  - {estudiante.nombre} (Matrícula: {estudiante.matricula})")

    def presentarse(self):
        print(f"Este es el grupo {self._numero_grupo}, para la asignatura {self._asignatura.nombre}, impartida por el profesor {self._profesor.nombre}.")

    @classmethod
    def cantidad_grupos(cls)->int:
        return cls._contador_grupos

