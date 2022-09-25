# This action replies on the queries like "What is <name>"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWhatIs(Action):
    def name(self) -> Text:
        return "action_what_is"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        print(f"action {self.name()} is being run")
        entities = tracker.latest_message["entities"]
        name_entity = None
        for entity in entities:
            if entity["entity"] == "name":
                name_entity = entity

        name = name_entity["value"] if name_entity else None
        if name:
            # TODO: return data about requested thing using Wikipedia API
            message = [
                {"type": "text", "content": f"Try to check about {name} here: "},
                {
                    "type": "link",
                    "text": f"https://en.wikipedia.org/wiki/{name}",
                    "link": f"https://en.wikipedia.org/wiki/{name}",
                },
                {"type": "text", "content": "."},
            ]
            dispatcher.utter_message(json_message=message)
        else:
            message = [
                {"type": "text", "content": f"I have no clue about it."},
            ]
            dispatcher.utter_message(json_message=message)

        return []
