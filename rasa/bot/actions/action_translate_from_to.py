# This action replies on queries like "Translate a <word> from <source_language> to <target_language>".

import datetime
import logging
from typing import Any, Text, Dict, List
from .utils import find_entity

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

logger = logging.getLogger(__name__)


class ActionWhatIs(Action):
    def name(self) -> Text:
        return "action_translate_from_to"

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
        word_to_translate_entity = find_entity(entities, "word_to_translate")
        language_from_entity = find_entity(entities, "language", "from")
        language_to_entity = find_entity(entities, "language", "to")

        word_to_translate = (
            word_to_translate_entity["value"] if word_to_translate_entity else None
        )
        language_from = language_from_entity["value"] if language_from_entity else None
        language_to = language_to_entity["value"] if language_to_entity else None

        # the confidence of language roles "from" and "to" is sometimes low, i.e. less than 60%.
        # TODO: check how to increase confidence of entity role detection. Probably, makes sense to add more samples.
        # if word_to_translate and language_from and language_to:
        if word_to_translate:
            # TODO: translate text using google translator api
            message = [
                {
                    "type": "text",
                    "content": f"Dude, ask Google or something. I'm not a translator!",
                },
                {
                    "type": "text",
                    "content": f' Try to check about "{word_to_translate}" here: ',
                },
                {
                    "type": "link",
                    "text": f"https://translate.google.com/",
                    "link": f"https://translate.google.com/",
                },
                {"type": "text", "content": "."},
            ]
            dispatcher.utter_message(json_message=message)
        else:
            message = [
                {
                    "type": "text",
                    "content": f"I have no clue about it. Try to ask Google for the translation, dude.",
                },
            ]
            dispatcher.utter_message(json_message=message)

        return []
