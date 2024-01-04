# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCumprimento(Action):
    def name(self):
        return "action_cumprimento"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Olá! Como posso ajudar?")
        return []

class ActionDespedida(Action):
    def name(self):
        return "action_despedida"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Até mais! Se precisar, estou por aqui.")
        return []
