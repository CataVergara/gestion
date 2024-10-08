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
        tk.Label(self.root, text="Estudiante:").grid(row=0, column=0)
        self.entry_nombre_estudiante = tk.Entry(self.root)
        self.entry_nombre_estudiante.grid(row=0, column=1)

        tk.Label(self.root, text="Apellido:").grid(row=1, column=0)
        self.entry_apellido_estudiante = tk.Entry(self.root)
        self.entry_apellido_estudiante.grid(row=1, column=1)

        tk.Label(self.root, text="Matrícula:").grid(row=2, column=0)
        self.entry_matricula = tk.Entry(self.root)
        self.entry_matricula.grid(row=2, column=1)

        tk.Label(self.root, text="Carrera:").grid(row=3, column=0)
        self.entry_carrera = tk.Entry(self.root)
        self.entry_carrera.grid(row=3, column=1)

        tk.Label(self.root, text="Semestre:").grid(row=4, column=0)
        self.entry_semestre = tk.Entry(self.root)
        self.entry_semestre.grid(row=4, column=1)

        tk.Button(self.root, text="Agregar Estudiante", command=self.agregar_estudiante).grid(row=5, column=0, columnspan=2)

        tk.Label(self.root, text="Profesor:").grid(row=6, column=0)
        self.entry_nombre_profesor = tk.Entry(self.root)
        self.entry_nombre_profesor.grid(row=6, column=1)

        tk.Label(self.root, text="Apellido:").grid(row=7, column=0)
        self.entry_apellido_profesor = tk.Entry(self.root)
        self.entry_apellido_profesor.grid(row=7, column=1)

        tk.Label(self.root, text="Número Empleado:").grid(row=8, column=0)
        self.entry_numero_empleado = tk.Entry(self.root)
        self.entry_numero_empleado.grid(row=8, column=1)

        tk.Label(self.root, text="Departamento:").grid(row=9, column=0)
        self.entry_departamento = tk.Entry(self.root)
        self.entry_departamento.grid(row=9, column=1)

        tk.Button(self.root, text="Agregar Profesor", command=self.agregar_profesor).grid(row=10, column=0, columnspan=2)

        tk.Label(self.root, text="Asignatura:").grid(row=11, column=0)
        self.entry_nombre_asignatura = tk.Entry(self.root)
        self.entry_nombre_asignatura.grid(row=11, column=1)

        tk.Label(self.root, text="Código:").grid(row=12, column=0)
        self.entry_codigo_asignatura = tk.Entry(self.root)
        self.entry_codigo_asignatura.grid(row=12, column=1)

        tk.Label(self.root, text="Créditos:").grid(row=13, column=0)
        self.entry_creditos = tk.Entry(self.root)
        self.entry_creditos.grid(row=13, column=1)

        tk.Button(self.root, text="Agregar Asignatura", command=self.agregar_asignatura).grid(row=14, column=0, columnspan=2)

        tk.Label(self.root, text="Grupo:").grid(row=15, column=0)
        self.entry_numero_grupo = tk.Entry(self.root)
        self.entry_numero_grupo.grid(row=15, column=1)

        tk.Label(self.root, text="Asignatura (Código):").grid(row=16, column=0)
        self.entry_asignatura_grupo = tk.Entry(self.root)
        self.entry_asignatura_grupo.grid(row=16, column=1)

        tk.Label(self.root, text="Profesor (Número):").grid(row=17, column=0)
        self.entry_profesor_grupo = tk.Entry(self.root)
        self.entry_profesor_grupo.grid(row=17, column=1)

        tk.Button(self.root, text="Agregar Grupo", command=self.agregar_grupo).grid(row=18, column=0, columnspan=2)

        tk.Label(self.root, text="Programa Académico:").grid(row=19, column=0)
        self.entry_nombre_programa = tk.Entry(self.root)
        self.entry_nombre_programa.grid(row=19, column=1)

        tk.Label(self.root, text="Código:").grid(row=20, column=0)
        self.entry_codigo_programa = tk.Entry(self.root)
        self.entry_codigo_programa.grid(row=20, column=1)

        tk.Button(self.root, text="Agregar Programa Académico", command=self.agregar_programa).grid(row=21, column=0, columnspan=2)

        tk.Button(self.root, text="Mostrar Información", command=self.mostrar_informacion).grid(row=22, column=0, columnspan=2)

    def agregar_estudiante(self):
        nombre = self.entry_nombre_estudiante.get()
        apellido = self.entry_apellido_estudiante.get()
        matricula = self.entry_matricula.get()
        carrera = self.entry_carrera.get()
        semestre = int(self.entry_semestre.get())

            
        if not nombre or not apellido or not matricula or not carrera or not semestre:
            messagebox.showerror("Error", "Todos los campos del estudiante son obligatorios.")
            return
        
        if not semestre.isdigit() or int(semestre) <= 0:
            messagebox.showerror("Error", "El semestre debe ser un número entero positivo.")
            return

        
        nuevo_estudiante = Estudiante(nombre, apellido, "2000-01-01", matricula, carrera, int(semestre))
        self.estudiantes.append(nuevo_estudiante)
        messagebox.showinfo("Éxito", "Estudiante agregado exitosamente!")
            
    

    def agregar_profesor(self):
        nombre = self.entry_nombre_profesor.get()
        apellido = self.entry_apellido_profesor.get()
        numero_empleado = self.entry_numero_empleado.get()
        departamento = self.entry_departamento.get()

        
        if not nombre or not apellido or not numero_empleado or not departamento:
            messagebox.showerror("Error", "Todos los campos del profesor son obligatorios.")
            return
        
        if not numero_empleado.isdigit():
            messagebox.showerror("Error", "El número de empleado debe ser un número entero.")
            return
        
        nuevo_profesor = Profesor(nombre, apellido, "1985-01-01", numero_empleado, departamento)
        self.profesores.append(nuevo_profesor)
        messagebox.showinfo("Éxito", "Profesor agregado exitosamente!")

    def agregar_asignatura(self):
        nombre = self.entry_nombre_asignatura.get()
        codigo = self.entry_codigo_asignatura.get()
        creditos = int(self.entry_creditos.get())

        Validaciones
        if not nombre or not codigo or not creditos:
            messagebox.showerror("Error", "Todos los campos de la asignatura son obligatorios.")
            return
        
        if not creditos.isdigit() or int(creditos) <= 0:
            messagebox.showerror("Error", "Los créditos deben ser un número entero positivo.")
            return
            
        nueva_asignatura = Asignatura(nombre, codigo, int(creditos))
        self.asignaturas.append(nueva_asignatura)
        messagebox.showinfo("Éxito", "Asignatura agregada exitosamente!")
        

    def agregar_grupo(self):
        numero_grupo = int(self.entry_numero_grupo.get())
        codigo_asignatura = self.entry_asignatura_grupo.get()
        numero_empleado = self.entry_profesor_grupo.get()
        
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
