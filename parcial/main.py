import random
import json
import api
from usuario import Usuario
from transacciones import Transaccion
from libroOrdenes import LibroOrdenes
from procesadorTx import ProcesadorTransacciones
from api import lista_Cryptos
from collections import deque

libro = LibroOrdenes()




cryptosFormateadas = []
for d in lista_Cryptos:    
        symbol = d["symbol"]
        price = float(d["price_usd"])
        cryptosFormateadas.append({"symbol": symbol, "price_usd": price})

historialTransaccion = []
usuarios = {
    1: Usuario(1,"juan",1000000,1000000+4000),
    2: Usuario(2, "matias",150000,150000*4000)
}

for i in range (10):
    crypto = random.choice(cryptosFormateadas)
    simbolo = crypto["symbol"]
    precio = float(crypto["price_usd"])


    Usuario_id = random.choice(list(usuarios.keys()))
    tipo = random.choice(["compra","venta"])
    cantidad = random.randint(1,10)

    transaccion = Transaccion(tipo,Usuario_id,simbolo, cantidad, precio,)
    libro.encolar(transaccion)

    historialTransaccion.append({  
    "usuario_id": Usuario_id,
    "tipo": tipo, 
    "simbolo": simbolo,
    "cantidad": cantidad,
    "precio_unitario": precio,
    }
      )
    with open("historial.json", 'w') as file:  # escribir en json
            json.dump(historialTransaccion,file,indent=4)  


            




procesador = ProcesadorTransacciones(usuarios,api.lista_Cryptos)
procesador.procesar(libro)


for z in usuarios.values():
    print(z)



import json

reporte = {}

for user_id, usuario in usuarios.items():
    historial =[]
    reporte[user_id] = {
        "saldo en dolares": usuario.saldo_usd,
        "saldo en peso colombiano": usuario.saldo_usd*4000,
        "portafolio": usuario.portafolio,
        "historial": [
            {
                "tipo": transaccion.tipo,
                "simbolo de compra": transaccion.simbolo,
                "cantidad comprada o vendida": transaccion.cantidad,
                "precio unitario": transaccion.precio_unitario,
                "total dolares": transaccion.total_usd()
            }

                 
            ]
    }


with open("reporte.json", "w") as f:
    json.dump(reporte, f, indent=4)




