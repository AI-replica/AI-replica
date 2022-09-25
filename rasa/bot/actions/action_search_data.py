# This is a custom action that searches answers in bot's data.

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from ai_replica.common import get_answer


class ActionSearchData(Action):
    def name(self) -> Text:
        return "action_search_data"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        print(f"action {self.name()} is being run")
        text = tracker.latest_message["text"]
        personal_question = text.replace("Tell me about ", "")
        bot_answer = get_answer(personal_question)
        # dispatcher.utter_message(text="Thinking...")
        dispatcher.utter_message(text=bot_answer)

        return []
