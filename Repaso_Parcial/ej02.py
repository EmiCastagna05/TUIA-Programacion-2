class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        
# a) Agregar a la clase Tarea un metodo para transformar la tarea en un string
    def __str__(self) -> str:
        return f"El titulo es: {self.titulo}. \nLa descripcion es: {self.descripcion}\n"

# b) Permitir unir dos tareas en una con el + concatenando sus titulos y descripciones.
    def __add__(self, other: 'Tarea') -> 'Tarea':
        return self.titulo +  " | " + other.titulo, self.descripcion + " | " + other.descripcion
        
# c) Crear una nueva clase TareaPrioritaria la cual hereda los metodos de Tarea pero en este
# caso permite guardar la prioridad de cada tarea siendo la 0 la mas alta.
class TareaPrioritaria(Tarea):
    def __init__(self, titulo, descripcion, prioridad) -> None:
        super().__init__(titulo, descripcion)
        self.prioridad = prioridad
        
    def __str__(self) -> str:
        return super().__str__() + f"La prioridad es: {self.prioridad}\n"
    
    def __add__(self, other: 'TareaPrioritaria') -> 'TareaPrioritaria':
        nuevo_titulo, nueva_descripcion = super().__add__(other)
        nueva_prioridad = str(self.prioridad) + " | " + str(other.prioridad)
        return TareaPrioritaria(nuevo_titulo, nueva_descripcion, nueva_prioridad)
    
# d) Agregar un metodo a TareaPrioritaria que las compare por prioridad. Una tarea antecede a otra si su prioridad es mas alta.
    def compararPrioridad(self, other: 'TareaPrioritaria') -> 'TareaPrioritaria':
        if self.prioridad > other.prioridad:
            return f"TAREA PRIORITARIA\nTitulo: {self.titulo}\nDescripcion: {self.descripcion}\nPrioridad: {self.prioridad}\n\nOTRA TAREA\nTitulo: {other.titulo}\nDescripcion: {other.descripcion}\nPrioridad: {other.prioridad}"
        else:
            return f"TAREA PRIORITARIA\nTitulo: {other.titulo}\nDescripcion: {other.descripcion}\nPrioridad: {other.prioridad}\n\nOTRA TAREA\nTitulo: {self.titulo}\nDescripcion: {self.descripcion}\nPrioridad: {self.prioridad}"

tarea1 = Tarea("Parcial", "Parcial de programacion 2")
tarea2 = Tarea("Presentacion", "Presentacion de Introduccion a IA")
# print(tarea1 + tarea2)
# print()

tareaP1 = TareaPrioritaria("Parcial", "Parcial de programacion 2", 7)
tareaP2 = TareaPrioritaria("Presentacion", "Presentacion de Introduccion a IA", 5)
print(tareaP1.compararPrioridad(tareaP2))
