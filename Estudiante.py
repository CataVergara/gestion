from Persona import Persona

class Estudiante(Persona):
    _contador_estudiantes:int = 0

    def __init__(self, nombre:str, apellido:str, fecha_de_nacimiento:str, matricula:str, carrera:str, semestre:int):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self._matricula = matricula
        self._carrera = carrera
        self._semestre = semestre

        Estudiante._contador_estudiantes += 1

    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula_setter):
        self._matricula = matricula_setter

    @property
    def carrera(self):
        return self._carrera
    
    @carrera.setter
    def carrera(self, carrera_setter):
        self._carrera = carrera_setter

    @property
    def semestre(self):
        return self._semestre
    
    @semestre.setter
    def semestre(self, semestre_setter):
        self._semestre = semestre_setter

    def estudiar(self, materia:str, horas:int):
        return f"El estudiante {self._nombre} está estudiando {materia} por {horas} horas."

    # Estudiante hereda el metodo presentarse de Persona
    def presentarse(self):
        return f"{super().presentarse()}. Mi matrícula es: {self._matricula}, de la carrera de {self._carrera} y el semestre numero {self._semestre}."

    @classmethod
    def cantidad_estudiantes(cls)->int:
        return cls._contador_estudiantes
