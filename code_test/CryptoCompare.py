import requests


headers = {
                'X-CMC_PRO_API_KEY': 'API_KEY',
                'Accepts': 'application/json'
        }

paramsMXN = {
        'start': '1',
        'limit': '200',
        'convert': 'MXN'                
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = paramsMXN, headers = headers).json()
coins =  json['data']

CryptoName = "DOGE"
CryptoName2 = "BTC"

for coin in coins:
    if coin['symbol'] == CryptoName:
        VAR1 = round(coin['quote']['MXN']['price'],4)
        CryptoName = coin['name']
    if coin['symbol'] == CryptoName2:
        VAR2 = round(coin['quote']['MXN']['price'],4)
        CryptoName2 = coin['name']

VAR3 = VAR1/VAR2


print("El " + CryptoName + " es aproximadamente " + str(format(VAR3,'.8f')) + " " +CryptoName2 +"s")