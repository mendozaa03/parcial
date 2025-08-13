from stack import Stack

class Usuario:
    def __init__(self, id, nombre, saldo_usd, saldoCop):
        self.id = id
        self.nombre = nombre
        self.saldo_usd = saldo_usd
        self.portafolio = {}  # {simbolo: cantidad}
        self.historial = Stack()  # pila de transacciones
        self.saldoCop = saldoCop

    def agregar_activo(self, simbolo, cantidad):
        self.portafolio[simbolo] = round(self.portafolio.get(simbolo, 0) + cantidad, 8)

    def quitar_activo(self, simbolo, cantidad):
        if simbolo in self.portafolio:
            self.portafolio[simbolo] -= cantidad
            if self.portafolio[simbolo] <= 0:
                del self.portafolio[simbolo]

    def agregar_historial(self, transaccion):
        self.historial.push(transaccion)
