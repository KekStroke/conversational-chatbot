from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

class ActionCollectFeedback(Action):
    def name(self) -> Text:
        return "action_collect_feedback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        feedback = tracker.latest_message['text']

        print(f'Feedback message \"{feedback}\" received!')

        # Respond to the user
        dispatcher.utter_message("Thanks for your feedback!")

        return []
