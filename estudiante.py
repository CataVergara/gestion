from Persona import Persona


class Estudiante(Persona):
    contador_estudiantes = 0

    def __init__(self, nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        Estudiante.contador_estudiantes += 1

    @property
    def matricula(self):
        return self._matricula

    @property
    def carrera(self):
        return self._carrera

    @property
    def semestre(self):
        return self._semestre

    def estudiar(self, materia, horas):
        return f"El estudiante {self._nombre} está estudiando {materia} por {horas} horas."

    @staticmethod
    def cantidad_estudiantes():
        return Estudiante.contador_estudiantes

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Matrícula: {self._matricula}, Carrera: {self._carrera}, Semestre: {self._semestre}"
