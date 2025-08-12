import requests
from collections import deque
import api


colaPrecios = deque()
for precios in api.listPrecios:
    
    colaPrecios.append(precios['price_usd']) 

print(colaPrecios)

 