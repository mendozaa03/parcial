import random
import json
import api
from usuario import Usuario
from transacciones import Transaccion
from libroOrdenes import LibroOrdenes
from procesadorTx import ProcesadorTransacciones

libro = LibroOrdenes()



usuarios = {
    1: Usuario(1,"juan",10000,1000+4000),
    2: Usuario(2, "matias",5000,5000*4000)
}


for i in range (10):
    crypto = random.choice(api.lista_Cryptos)
    simbolo = crypto["symbol"]
    precio = float(crypto["price_usd"])


    Usuario_id = random.choice(list(usuarios.keys()))
    tipo = random.choice(["compra","venta"])
    cantidad = random.randint(1,10)

    transaccion = Transaccion(Usuario_id, simbolo, cantidad, precio, tipo)
    libro.encolar(transaccion)



             



procesador = ProcesadorTransacciones(usuarios,api.lista_Cryptos)
procesador.procesar(libro)


for z in usuarios.values():
    print(z)




