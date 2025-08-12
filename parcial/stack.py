
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()  # Usamos deque para la pila
    
    def push(self, item):
        self.stack.append(item)  # Agregar un elemento al final de la pila
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Eliminar y devolver el último elemento
        else:
            return "La pila está vacía"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Ver el último elemento sin eliminarlo
        else:
            return "La pila está vacía"
    
    def is_empty(self):
        return len(self.stack) == 0  # Verificar si la pila está vacía
    
    def size(self):
        return len(self.stack)  # Obtener el número de elementos en la pila
