from Empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.habilidades = []

    def asignar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Habilidades: {self.habilidades}")