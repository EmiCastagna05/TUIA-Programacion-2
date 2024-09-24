class Pila:
    def __init__(self):
        """init"""
        self.datos = []

    def push(self, element):
        """Añado un elemento a la derecha"""
        self.datos.append(element)

    def pop(self):
        """
        Elimino el ultimo elemento
        Este metodo no se puede llamar si la pila esta vacia
        """
        return self.datos.pop()

    def is_empty(self) -> bool:
        """Verifico si la pila esta vacia"""
        return self.datos == []
    
class Cola:
    def __init__(self):
        """init"""
        self.datos = []

    def push(self, element):
        """Añado un elemento a la derecha"""
        self.datos.append(element)

    def pop(self):
        """
        Elimino el primer elemento
        Este metodo no se puede llamar si la cola esta vacia
        """
        return self.datos.pop(0)

    def is_empty(self) -> bool:
        """Verifico si la cola esta vacia"""
        return self.datos == []
    
c = Cola()
c.push(1)
# c.push(2)
# c.push(3)
# print(c.pop())
print(c.is_empty)
    
# p = Pila()
# print(p.is_empty())
# p.push(1)
# p.push(2)
# p.push(3)
# print(p.is_empty())
# print(help(Pila))
# print(p.pop())