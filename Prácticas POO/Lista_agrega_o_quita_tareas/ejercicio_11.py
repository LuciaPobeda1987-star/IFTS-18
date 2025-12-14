class ListaDeTareas:
    def __init__(self):
        # Atributo de instancia privado
        self.__lista_tareas = []

    # Método para agregar una tarea
    def agregarTarea(self, tarea):
        try:
            self.__lista_tareas.append(tarea)
            return "Tarea agregada correctamente a la lista"
        except Exception:
            return "La tarea no fue agregada a la lista"

    # Método para quitar una tarea
    def quitarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            return "Tarea eliminada correctamente de la lista"
        else:
            return "La tarea no fue eliminada de la lista"

    # Método para mostrar todas las tareas
    def mostrarTareas(self):
        return self.__lista_tareas

# Crear una instancia de ListaDeTareas
mi_lista = ListaDeTareas()

# Agregar tareas
print(mi_lista.agregarTarea("Comprar leche"))
print(mi_lista.agregarTarea("Estudiar para el examen"))
print(mi_lista.agregarTarea("Hacer ejercicio"))

# Eliminar una tarea existente
print(mi_lista.quitarTarea("Estudiar para el examen"))

# Intentar eliminar una tarea que no está en la lista
print(mi_lista.quitarTarea("Llamar al doctor"))

# Mostrar la lista de tareas final
print("Lista de tareas actual:")
for tarea in mi_lista.mostrarTareas():
    print(f"- {tarea}")