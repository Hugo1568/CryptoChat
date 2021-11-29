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
                'X-CMC_PRO_API_KEY': '199d6932-1299-498a-879e-fff878f21e89',
                'Accepts': 'application/json'
        }

        paramsMXN = {
                'start': '1',
                'limit': '6',
                'convert': 'MXN'
                }

        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        json = requests.get(url, params = paramsMXN, headers = headers).json()
        coins =  json['data']

        CryptoName = tracker.get_slot("crypto")
        lmao=str(CryptoName)
        
        for coin in coins:
            if coin['symbol'] == CryptoName:
                lmao = ("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n")
            if coin['slug'] == CryptoName:
                lmao = ("El precio del " + str(coin['slug']) + " es de: $" + str(round(coin['quote']['MXN']['price'],4) ) + " pesos mexicanos" + "\n")
            

        dispatcher.utter_message(text=lmao)

        return []


