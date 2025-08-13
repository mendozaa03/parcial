import usuario

class ProcesadorTransacciones:
    def __init__(self,usuarios,criptos):
        self.usuarios = usuarios
        self.criptos = criptos
        self.transaccionFallidas = []

    def procesar (self,libro):
        while libro.cola:
            transaccion = libro.desencolar()
            if self.validar(transaccion):
                self.aplicar(transaccion)
                self.usuarios[transaccion.usuario_id].agregar_historial(transaccion)
            else:
                print("transaccion invalida, el usuario no tiene suficientes monedas para vender o dinero para comprar")
                self.transaccionFallidas.append(transaccion)
    def validar(self,transaccion):
        usuario = self.usuarios[transaccion.usuario_id]
        if transaccion.tipo == "compra":
            return usuario.saldo_usd >= transaccion.total_usd()
        elif transaccion.tipo == "venta":
            return usuario.portafolio.get(transaccion.simbolo,0) >= transaccion.cantidad
        return False
    def aplicar(self, transaccion):
        usuario = self.usuarios[transaccion.usuario_id]
        if transaccion.tipo == "compra":
            usuario.saldo_usd -= transaccion.total_usd()
            usuario.agregar_activo(transaccion.simbolo, transaccion.cantidad)
        elif transaccion.tipo == "venta":
            usuario.saldo_usd += transaccion.total_usd()
            usuario.quitar_activo(transaccion.simbolo, transaccion.cantidad)

        

    

    