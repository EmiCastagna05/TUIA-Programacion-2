# Crear una clase ColaConPromedio que soporte las operaciones de Cola
# incluya el metodo obtener promedio() que devuelva el promedio de los elementos de la cola y
# funciona en tiempo constante.

class colaConPromedio():
    def __init__(self):
        """init"""
        self.elementos = []
        
    def push(self, elemento):
        """Añado un elemento a la derecha"""
        self.elementos.append(elemento)
    
    def pop(self):
        """
        Elimino el ultimo elemento
        Este metodo no se puede llamar si la pila esta vacia
        """
        self.elementos.pop(0)
        
    def is_empty(self) -> bool:
        """Verifico si la cola esta vacia"""
        return self.elementos == []
    
    def obtenerPromedio(self) -> int:
        prom = 0
        cont = 0
        size = len(self.elementos)
        
        if size == 0:
            return "La cola esta vacia. No se puede calcular un promedio \nUsa el metodo push para insertar nuevos elementos"
        else:
            for i in self.elementos:
                cont += i
            
            prom = cont / size
            return f"El promedio es {prom}"
    
cola = colaConPromedio()
cola.push(5)
cola.push(6)
cola.push(5)
cola.push(7)
cola.push(1)
print(cola.obtenerPromedio())
