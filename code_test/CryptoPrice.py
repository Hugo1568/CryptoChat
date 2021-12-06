import requests
import json
from requests import Session
import secrets
from pprint import pprint as pp

# Build up a class so we can easily make the REST API calls

class CMC:
    #https://coinmarketcap.com/api/documentation/v1/
    def __init__(self,):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'X-CMC_PRO_API_KEY': 'API_KEY', 'Accepts': 'application/json'}
        self.session = Session()
        self.session.headers.update(self.headers)
    
    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        with open('data.json', 'w') as f:
                json.dump(data, f)
        return data
        
    def getPrice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url, params=parameters)
        data = r.json()['data']
        return data
    
    
cmc = CMC()

pp(cmc.getAllCoins())