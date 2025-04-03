def agregar_estudiante(estudiantes):
    """
    Agrega un nuevo estudiante al registro.
    """
    nombre = input("Introduce el nombre del estudiante: ")
    edad = input("Introduce la edad del estudiante: ")
    try:
        calificaciones = list(map(float, input("Introduce las calificaciones separadas por comas: ").split(',')))
        estudiantes.append({"nombre": nombre, "edad": edad, "calificaciones": calificaciones})
        print("Estudiante agregado exitosamente.")
    except ValueError:
        print("Por favor, introduce calificaciones válidas.")

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    """
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

def mostrar_estudiantes_con_promedio(estudiantes, valor):
    """
    Muestra estudiantes con promedio mayor a un valor dado.
    """
    print(f"Estudiantes con promedio mayor a {valor}:")
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["calificaciones"])
        if promedio > valor:
            print(f"Nombre: {estudiante['nombre']}, Promedio: {promedio:.2f}")

def buscar_estudiante(estudiantes, nombre):
    """
    Busca un estudiante por nombre.
    """
    print(f"Resultados de búsqueda para '{nombre}':")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            promedio = calcular_promedio(estudiante["calificaciones"])
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {promedio:.2f}")
            return
    print("Estudiante no encontrado.")

def main():
    estudiantes = []
    while True:
        print("\nMenú:")
        print("1. Agregar nuevo estudiante")
        print("2. Calcular promedio de calificaciones de cada estudiante")
        print("3. Mostrar estudiantes con promedio mayor a un valor dado")
        print("4. Buscar estudiante por nombre")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            print("Promedios de estudiantes:")
            for estudiante in estudiantes:
                promedio = calcular_promedio(estudiante["calificaciones"])
                print(f"Nombre: {estudiante['nombre']}, Promedio: {promedio:.2f}")
        elif opcion == "3":
            try:
                valor = float(input("Introduce el valor del promedio: "))
                mostrar_estudiantes_con_promedio(estudiantes, valor)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "4":
            nombre = input("Introduce el nombre del estudiante a buscar: ")
            buscar_estudiante(estudiantes, nombre)
        elif opcion == "5":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()