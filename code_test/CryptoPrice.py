import requests
import time

headers = {
        'X-CMC_PRO_API_KEY': '199d6932-1299-498a-879e-fff878f21e89',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '6',
        'convert': 'USD'
        }

paramsMXN = {
        'start': '1',
        'limit': '6',
        'convert': 'MXN'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = paramsMXN, headers = headers).json()

coins =  json['data']

#Examples: BTC, ETH, USDT, BNB, ADA, DODGE
CryptoName = "BNB"

print("Datos de: " + str(CryptoName)+ "\n")
for coin in coins:
    if coin['symbol'] == CryptoName:
        print("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n") 

    #def ObtenerPrecio(self, msg):
