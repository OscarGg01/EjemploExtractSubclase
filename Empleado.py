class Empleado:
    def __init__(self, nombre, salario, habilidades=None):
        self.nombre = nombre
        self.salario = salario
        self.habilidades = habilidades  # Solo para desarrolladores
        self.tareas_administrativas = []  # Solo para administrativos

    def asignar_tarea_administrativa(self, tarea):
        if self.tareas_administrativas is not None:
            self.tareas_administrativas.append(tarea)
        else:
            raise ValueError("Este empleado no realiza tareas administrativas")

    def asignar_habilidad(self, habilidad):
        if self.habilidades is not None:
            self.habilidades.append(habilidad)
        else:
            raise ValueError("Este empleado no es un desarrollador")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")
        if self.habilidades:
            print(f"Habilidades: {self.habilidades}")
        if self.tareas_administrativas:
            print(f"Tareas Administrativas: {self.tareas_administrativas}")
