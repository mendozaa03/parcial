from collections import deque

class LibroOrdenes:
    def __init__(self):
        self.cola = deque()

    def encolar(self, transaccion):
        self.cola.append(transaccion)

    def desencolar(self):
        if self.cola:
            return self.cola.popleft()
        return None
