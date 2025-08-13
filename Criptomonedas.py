import random

class Criptomoneda:
    
    def __init__(self,ID, simbolo,nombre, precio_usd):
        self.simbolo = simbolo
        self.precio_usd = float(precio_usd)
        self.ID = ID
        self.nombre = nombre 


    def fluctuar(self):
        cambio = random.uniform(-0.05, 0.05)  
        self.precio_usd = round(max(0.01,self.precio_usd* (1 + cambio),2))
