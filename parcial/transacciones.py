class Transaccion:
    def __init__(self, tipo, usuario_id, simbolo, cantidad, precio_unitario):
        self.tipo = tipo  # "COMPRA" o "VENTA"
        self.usuario_id = usuario_id
        self.simbolo = simbolo
        self.cantidad = float(cantidad)
        self.precio_unitario = precio_unitario

    def total_usd(self):
        return round(self.cantidad * self.precio_unitario, 2)