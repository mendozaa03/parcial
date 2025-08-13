import random
import json
from collections import deque
import requests
from collections import deque


url = "https://api.coinlore.net/api/tickers/"
response = requests.get(url)
data = response.json()
lista_Cryptos = data['data']
colaPrecios = deque()
listPrecios = data['data']
colaPrecios = deque()
for precios in listPrecios:
    colaPrecios.append(precios['price_usd'])


colaNombre = deque 




colaNombre = deque()
for nombre in listPrecios:
    colaNombre.append(nombre['name'])


colaTransacciones = deque()
historialTX = deque()
