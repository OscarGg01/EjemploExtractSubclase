from Empleado import Empleado

class EmpleadoAdministrativo(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.tareas_administrativas = []

    def asignar_tarea_administrativa(self, tarea):
        self.tareas_administrativas.append(tarea)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tareas Administrativas: {self.tareas_administrativas}")
