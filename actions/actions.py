from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ask_program(Action):

    def name(self) -> Text:
        return "action_ask_program"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # program_entity = next(tracker.get_latest_entity_values('program'), None)

        # if program_entity: 
        #     dispatcher.utter_message(text=f"You have selected {program_entity} as your program choice")
        # else:
        #     dispatcher.utter_message(text="I am sorry, I could not detect program choice")

        # return []

        dispatcher.utter_message(text="Which kind of program would you like to know?")
        
        return []

class ConfirmAskProgramAction(Action):
    def name(self) -> Text:
        return "action_confirm_program"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        program_entity = next(tracker.get_latest_entity_values('program'), None)

        if program_entity: 
            dispatcher.utter_message(text=f"You chose {program_entity}")
        else:
            dispatcher.utter_message(text="I am sorry, I could not detect program choice")

        return []





class ActionLookupCourse(Action):
    def name(self) -> Text:
        return "action_lookup_course"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        course = tracker.get_slot("course_name")
        program = tracker.get_slot("program_type")
        
        # Replace with API/database call
        details = f"The {program} in {course} includes 10 core courses and 5 electives."
        
        dispatcher.utter_message(text=details)
        return []

class ActionLookupFees(Action):
    def name(self) -> Text:
        return "action_lookup_fees"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        fee_type = tracker.get_slot("fee_type")
        course = tracker.get_slot("course_name")
        
        # Example mock response
        if fee_type == "tuition":
            dispatcher.utter_message(text=f"Tuition for {course} is $5,000 per semester.")
        return []
    
class ActionLookupProgramFee(Action):
    def name(self) -> Text:
        return "action_lookup_program_fee"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict):
        program_type = tracker.get_slot("program_type")
        major = tracker.get_slot("major")

        fee_structure = {
            "Associate": 250,
            "Bachelor": 500
        }

        amount = fee_structure.get(program_type, 0)

        dispatcher.utter_message(
            text=f"The annual fee for the {program_type} program in {major} is ${amount}."
        )
        return []

