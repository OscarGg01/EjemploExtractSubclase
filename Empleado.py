class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")


class EmpleadoAdministrativo(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.tareas_administrativas = []

    def asignar_tarea_administrativa(self, tarea):
        self.tareas_administrativas.append(tarea)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tareas Administrativas: {self.tareas_administrativas}")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.habilidades = []

    def asignar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidades: {self.habilidades}")
