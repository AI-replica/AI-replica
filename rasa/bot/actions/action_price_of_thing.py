# This action replies on the queries like "What is price of <thing>"

import datetime
import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ActionWhatIs(Action):
    def name(self) -> Text:
        return "action_price_of_thing"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        logger.info(
            f"[{datetime.datetime.now():%Y-%m-%d}] action {self.name()} is being run"
        )
        entities = tracker.latest_message["entities"]
        thing_entity = None
        for entity in entities:
            if entity["entity"] == "thing":
                thing_entity = entity

        thing = thing_entity["value"] if thing_entity else None
        if thing:
            # TODO: return data about requested thing using Wikipedia API
            message = [
                {"type": "text", "content": f"Try to check about {thing} here: "},
                {
                    "type": "link",
                    "text": f"https://en.wikipedia.org/wiki/{thing}",
                    "link": f"https://en.wikipedia.org/wiki/{thing}",
                },
                {"type": "text", "content": "."},
            ]
            dispatcher.utter_message(json_message=message)
        else:
            message = [
                {
                    "type": "text",
                    "content": f"I have no clue about the price of this thing. Try to ask Google, dude.",
                },
            ]
            dispatcher.utter_message(json_message=message)

        return []
