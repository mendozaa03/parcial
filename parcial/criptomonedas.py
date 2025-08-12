import random
from collections import dequeu
colaPrecios = dequeu

class Criptomoneda:
    
    def __init__(self,ID, simbolo,nombre, precio_usd):
        self.simbolo = simbolo
        self.precio_usd = precio_usd
        self.ID = ID
        self.nombre = nombre 


    def fluctuar(self):
        cambio = random.uniform(-0.05, 0.05)  
        self.precio_usd = (colaPrecios + cambio)
