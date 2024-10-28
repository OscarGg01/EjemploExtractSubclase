from Empleado import EmpleadoAdministrativo
from Empleado import Desarrollador


def crear_empleado():
    tipo = input("Ingrese el tipo de empleado (administrativo/desarrollador): ").strip().lower()
    nombre = input("Ingrese el nombre del empleado: ").strip()
    salario = float(input("Ingrese el salario del empleado: "))

    if tipo == "administrativo":
        empleado = EmpleadoAdministrativo(nombre, salario)
        while True:
            tarea = input("Ingrese una tarea administrativa (o presione Enter para finalizar): ").strip()
            if not tarea:
                break
            empleado.asignar_tarea_administrativa(tarea)
    elif tipo == "desarrollador":
        empleado = Desarrollador(nombre, salario)
        while True:
            habilidad = input("Ingrese una habilidad (o presione Enter para finalizar): ").strip()
            if not habilidad:
                break
            empleado.asignar_habilidad(habilidad)
    else:
        print("Tipo de empleado no válido.")
        return None

    return empleado


def main():
    empleados = []
    while True:
        empleados.append(crear_empleado())
        continuar = input("¿Desea ingresar otro empleado? (s/n): ").strip().lower()
        if continuar != "s":
            break

    print("\nInformación de los empleados:")
    for empleado in empleados:
        if empleado:
            empleado.mostrar_info()
            print("-" * 30)


if __name__ == "__main__":
    main()
