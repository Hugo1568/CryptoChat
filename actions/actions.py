# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
import requests
import re

CMC_API_KEY = "API_KEY"

class ActionCryptoPrice(Action):

    def name(self) -> Text:
        return "action_crypto_price"

    @staticmethod
    def fetch_slots(tracker: Tracker):
        #Collects slots on crypto price
        tracker.get_slot("crypto")


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {
                'X-CMC_PRO_API_KEY': CMC_API_KEY,
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

        CryptoName = str(tracker.get_slot("crypto"))
        if CryptoName is None:
            CryptoName = str(tracker.get_slot("crypto2"))
        if re.match(r'\b[a-zA-Z]{3,6}\b', CryptoName):
            CryptoName = CryptoName.upper()


        display_text="La moneda no se encontró, o no está en el top 200 de criptomonedas, intenta utilizar su símbolo. ejemplo: Bitcoin: BTC"
        if CryptoName is None:
            display_text="Te mamaste no hay token"
        if CryptoName is not None:
            for coin in coins:
                if coin['slug'] == CryptoName:
                    display_text = ("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n")
                if coin['name'] == CryptoName:
                    display_text = ("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n")
                if coin['symbol'] == CryptoName:
                    display_text = ("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n")
            

        dispatcher.utter_message(text=display_text)

        return []


class ActionCryptoCompare(Action):

    def name(self) -> Text:
        return "action_crypto_compare"

    @staticmethod
    def fetch_slots(tracker: Tracker):
        #Collects slots on crypto price
        tracker.get_slot("crypto", "crypto2")


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = {
                'X-CMC_PRO_API_KEY': CMC_API_KEY,
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

        CryptoName= str(tracker.get_slot("crypto"))
        CryptoName2= str(tracker.get_slot("crypto2"))

        if re.match(r'\b[a-zA-Z]{3,6}\b', CryptoName):
                        CryptoName = CryptoName.upper()
        if re.match(r'\b[a-zA-Z]{3,6}\b', CryptoName2):
                        CryptoName2 = CryptoName2.upper()


        display_text="La moneda no se encontró, o no está en el top 200 de criptomonedas, intenta utilizar su símbolo. ejemplo: Bitocin: BTC"
        for coin in coins:
            if coin['symbol'] == CryptoName or coin['slug'] == CryptoName or coin['name'] == CryptoName:
                VAR1 = round(coin['quote']['MXN']['price'],4)
                CryptoName = coin['name']
            if coin['slug'] == CryptoName:
                VAR1 = round(coin['quote']['MXN']['price'],4)
                CryptoName = coin['name']
            if coin['name'] == CryptoName:
                VAR1 = round(coin['quote']['MXN']['price'],4)
                CryptoName = coin['name']
            if coin['symbol'] == CryptoName2:
                VAR2 = round(coin['quote']['MXN']['price'],4)
                CryptoName2 = coin['name']
            if coin['slug'] == CryptoName2:
                VAR2 = round(coin['quote']['MXN']['price'],4)
                CryptoName2 = coin['name']
            if coin['name'] == CryptoName2:
                VAR2 = round(coin['quote']['MXN']['price'],4)
                CryptoName2 = coin['name']
        if VAR1 and VAR2 is not None:
            VAR3 = VAR1/VAR2
            display_text= ("El " + CryptoName + " es aproximadamente " + str(format(VAR3,'.8f')) + " " +CryptoName2 +"s")

        dispatcher.utter_message(text=display_text)

        return []


