import criptomonedas
import libroOrdenes
import api
import api
from usuario import Usuario
from libroOrdenes import LibroOrdenes
from transacciones import Transaccion
import random

# Inicializar usuarios
usuarios = {}
for i in range(3):
    u = Usuario(id=i, nombre=f"Usuario{i+1}", saldo_usd=1000, saldoCop=0)
    usuarios[u.id] = u

# Inicializar criptomonedas desde la API
precios = {}
simbolos = []
for cripto in api.lista_Cryptos:
    simbolos.append(cripto['symbol'])
    precios[cripto['symbol']] = float(cripto['price_usd'])

# Inicializar libro de órdenes
libro = LibroOrdenes()

# Simulación de 10 turnos
for turno in range(10):
    for cripto in criptos():
        cripto.fluctuar()






