from Persona import Persona

class Estudiante(Persona):
    contador_estudiantes = 0

    def __init__(self, nombre, apellido, fecha_de_nacimiento, matricula:str, carrera:str, semestre:int):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre
        Estudiante.contador_estudiantes += 1

    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def carrera(self):
        return self._carrera
    
    @carrera.setter
    def carrera(self, valor):
        self._carrera = valor

    @property
    def semestre(self):
        return self._semestre
    
    @semestre.setter
    def semestre(self, valor):
        self._semestre = valor

    def estudiar(self, materia:str, horas:int):
        return f"El estudiante {self._nombre} está estudiando {materia} por {horas} horas."

    @staticmethod
    def cantidad_estudiantes():
        return Estudiante.contador_estudiantes

    # Este metodo esta siendo heredado de la clase Asignatura, cuando en realidad Estudiante deberia tener el metodo presentarse de Persona
    # De hecho no hay ninguna referencia de la clase Asignatura en esta clase?
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Matrícula: {self._matricula}, Carrera: {self._carrera}, Semestre: {self._semestre}"
    
    # def presentarse(self):
    #     return super().presentarse(f"Hola, soy el estudiante {self.nombre} {self.apellido}")
