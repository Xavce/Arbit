import time
from config.exchanges_config import exchanges

class Details: 
    ws = ""
    currencies = ""
    def __init__ (self, exchangeName):
        self.ws = exchanges[exchangeName]["ws"]


info = Details("gateio")

print(info.ws)