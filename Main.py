import tkinter as tk
from tkinter import messagebox
from Persona import Persona
from Estudiante import Estudiante
from Profesor import Profesor
from Asignatura import Asignatura
from Grupo import Grupo
from ProgramaAcademico import ProgramaAcademico

# Clase principal de la aplicación
class GestionAcademicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión Académica")

        self.estudiantes = []
        self.profesores = []
        self.asignaturas = []
        self.grupos = []
        self.programas = []

        self.create_widgets()

    def create_widgets(self):

        # Entradas para ingresas los datos de los estudiantes

        tk.Label(self.root, text="Estudiante:").grid(row=0, column=0)
        self.entry_nombre_estudiante = tk.Entry(self.root)
        self.entry_nombre_estudiante.grid(row=0, column=1)

        tk.Label(self.root, text="Apellido:").grid(row=1, column=0)
        self.entry_apellido_estudiante = tk.Entry(self.root)
        self.entry_apellido_estudiante.grid(row=1, column=1)

        tk.Label(self.root, text="Fecha de nacimiento:").grid(row=2, column=0)
        self.entry_nacimiento_estudiante = tk.Entry(self.root)
        self.entry_nacimiento_estudiante.grid(row=2, column=1)

        tk.Label(self.root, text="Matrícula:").grid(row=3, column=0)
        self.entry_matricula = tk.Entry(self.root)
        self.entry_matricula.grid(row=3, column=1)

        tk.Label(self.root, text="Carrera:").grid(row=4, column=0)
        self.entry_carrera = tk.Entry(self.root)
        self.entry_carrera.grid(row=4, column=1)

        tk.Label(self.root, text="Semestre:").grid(row=5, column=0)
        self.entry_semestre = tk.Entry(self.root)
        self.entry_semestre.grid(row=5, column=1)

        tk.Button(self.root, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=6, column=0, columnspan=2)


        # Entradas para ingresas los datos de los profesores

        tk.Label(self.root, text="Profesor:").grid(row=7, column=0)
        self.entry_nombre_profesor = tk.Entry(self.root)
        self.entry_nombre_profesor.grid(row=7, column=1)

        tk.Label(self.root, text="Apellido:").grid(row=8, column=0)
        self.entry_apellido_profesor = tk.Entry(self.root)
        self.entry_apellido_profesor.grid(row=8, column=1)

        tk.Label(self.root, text="Fecha nacimiento:").grid(row=9, column=0)
        self.entry_nacimiento_profesor = tk.Entry(self.root)
        self.entry_nacimiento_profesor.grid(row=9, column=1)

        tk.Label(self.root, text="Número Empleado:").grid(row=10, column=0)
        self.entry_numero_empleado = tk.Entry(self.root)
        self.entry_numero_empleado.grid(row=10, column=1)

        tk.Label(self.root, text="Departamento:").grid(row=11, column=0)
        self.entry_departamento = tk.Entry(self.root)
        self.entry_departamento.grid(row=11, column=1)

        tk.Button(self.root, text="Agregar Profesor", command=self.agregar_profesor).grid(row=12, column=0, columnspan=2)


        # Entradas para ingresas los datos de las asignaturas

        tk.Label(self.root, text="Asignatura:").grid(row=13, column=0)
        self.entry_nombre_asignatura = tk.Entry(self.root)
        self.entry_nombre_asignatura.grid(row=13, column=1)

        tk.Label(self.root, text="Código:").grid(row=14, column=0)
        self.entry_codigo_asignatura = tk.Entry(self.root)
        self.entry_codigo_asignatura.grid(row=14, column=1)

        tk.Label(self.root, text="Créditos:").grid(row=15, column=0)
        self.entry_creditos = tk.Entry(self.root)
        self.entry_creditos.grid(row=15, column=1)

        tk.Button(self.root, text="Agregar Asignatura", command=self.agregar_asignatura).grid(row=16, column=0, columnspan=2)


        # Entradas para ingresas los datos de los grupos

        tk.Label(self.root, text="Grupo:").grid(row=17, column=0)
        self.entry_numero_grupo = tk.Entry(self.root)
        self.entry_numero_grupo.grid(row=17, column=1)

        tk.Label(self.root, text="Asignatura (Código):").grid(row=18, column=0)
        self.entry_asignatura_grupo = tk.Entry(self.root)
        self.entry_asignatura_grupo.grid(row=18, column=1)

        tk.Label(self.root, text="Profesor (Número):").grid(row=19, column=0)
        self.entry_profesor_grupo = tk.Entry(self.root)
        self.entry_profesor_grupo.grid(row=19, column=1)

        tk.Button(self.root, text="Agregar Grupo", command=self.agregar_grupo).grid(row=20, column=0, columnspan=2)


        # Entradas para ingresas los datos del programa academico

        tk.Label(self.root, text="Programa Académico:").grid(row=21, column=0)
        self.entry_nombre_programa = tk.Entry(self.root)
        self.entry_nombre_programa.grid(row=21, column=1)

        tk.Label(self.root, text="Código:").grid(row=22, column=0)
        self.entry_codigo_programa = tk.Entry(self.root)
        self.entry_codigo_programa.grid(row=22, column=1)

        tk.Button(self.root, text="Agregar Programa Académico", command=self.agregar_programa).grid(row=23, column=0, columnspan=2)


        # Mostrar toda la informacion agregada anteriormente
        tk.Button(self.root, text="Mostrar Información", command=self.mostrar_informacion).grid(row=24, column=0, columnspan=2)

    def agregar_estudiante(self):
        nombre = self.entry_nombre_estudiante.get().strip()
        apellido = self.entry_apellido_estudiante.get().strip()
        fecha_nacimiento = self.entry_nacimiento_estudiante.get().strip
        matricula = self.entry_matricula.get().strip()
        carrera = self.entry_carrera.get().strip()
        semestre = self.entry_semestre.get().strip()  
        
        if not nombre or not apellido or not matricula or not carrera or not semestre:
            messagebox.showerror("Error", "Todos los campos del estudiante son obligatorios.")
            return
        
        try:
            semestre = int(semestre)  
        except ValueError:
            messagebox.showerror("Error", "El semestre debe ser un número entero.")
            return

        if semestre <= 0:
            messagebox.showerror("Error", "El semestre debe ser mayor que cero.")
            return
        
        nuevo_estudiante = Estudiante(nombre, apellido, fecha_nacimiento, matricula, carrera, semestre)
        self.estudiantes.append(nuevo_estudiante)
        messagebox.showinfo("Éxito", "Estudiante agregado exitosamente!")

    def agregar_profesor(self):
        nombre = self.entry_nombre_profesor.get().strip()
        apellido = self.entry_apellido_profesor.get().strip()
        fecha_nacimiento = self.entry_nacimiento_profesor.get().strip()
        numero_empleado = self.entry_numero_empleado.get().strip()
        departamento = self.entry_departamento.get().strip()

        if not nombre or not apellido or not numero_empleado or not departamento:
            messagebox.showerror("Error", "Todos los campos del profesor son obligatorios.")
            return

        if not numero_empleado.isdigit():
            messagebox.showerror("Error", "El número de empleado debe ser un número entero.")
            return

        nuevo_profesor = Profesor(nombre, apellido, fecha_nacimiento, numero_empleado, departamento)
        self.profesores.append(nuevo_profesor)
        messagebox.showinfo("Éxito", "Profesor agregado exitosamente!")


    def agregar_asignatura(self):
        nombre = self.entry_nombre_asignatura.get().strip()
        codigo = self.entry_codigo_asignatura.get().strip()
        creditos = self.entry_creditos.get().strip()

        if not nombre or not codigo or not creditos:
            messagebox.showerror("Error", "Todos los campos de la asignatura son obligatorios.")
            return

        try:
            creditos = int(creditos)
            if creditos <= 0:
                raise ValueError  
        except ValueError:
            messagebox.showerror("Error", "Los créditos deben ser un número entero positivo.")
            return

        nueva_asignatura = Asignatura(nombre, codigo, creditos)
        self.asignaturas.append(nueva_asignatura)
        messagebox.showinfo("Éxito", "Asignatura agregada exitosamente!")

    def agregar_grupo(self):
        numero_grupo = int(self.entry_numero_grupo.get())
        codigo_asignatura = self.entry_asignatura_grupo.get()
        numero_empleado = self.entry_profesor_grupo.get()

        
        if any(grupo.numero_grupo == numero_grupo for grupo in self.grupos):
            messagebox.showerror("Error", "El grupo ya existe.")
            return
        
        asignatura = next((asignatura for asignatura in self.asignaturas if asignatura.codigo == codigo_asignatura), None)
        profesor = next((profesor for profesor in self.profesores if profesor.numero_empleado == numero_empleado), None)
        
        if asignatura and profesor:
            nuevo_grupo = Grupo(numero_grupo, asignatura, profesor)
            self.grupos.append(nuevo_grupo)
            messagebox.showinfo("Éxito", "Grupo agregado exitosamente!")
        else:
            messagebox.showerror("Error", "Asignatura o profesor no encontrado.")



    def agregar_programa(self):
        nombre = self.entry_nombre_programa.get()
        codigo = self.entry_codigo_programa.get()
        
        nuevo_programa = ProgramaAcademico(nombre, codigo)
        self.programas.append(nuevo_programa)
        messagebox.showinfo("Éxito", "Programa académico agregado exitosamente!")

    def mostrar_informacion(self):
        info = ""
        info += "Estudiantes:\n" + "\n".join([estudiante.presentarse() for estudiante in self.estudiantes]) + "\n"
        info += "Profesores:\n" + "\n".join([profesor.presentarse() for profesor in self.profesores]) + "\n"
        info += "Asignaturas:\n" + "\n".join([asignatura.mostrar_informacion() for asignatura in self.asignaturas]) + "\n"
        info += "Grupos:\n" + "\n".join([grupo.mostrar_grupo() for grupo in self.grupos]) + "\n"
        info += "Programas Académicos:\n" + "\n".join([programa.mostrar_programa() for programa in self.programas]) + "\n"
        
        messagebox.showinfo("Información", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionAcademicaApp(root)
    root.mainloop()
