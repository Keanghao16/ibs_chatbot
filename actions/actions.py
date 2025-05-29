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
        program = tracker.get_slot("program_type")
        major = tracker.get_slot("major")

        # Prompt for missing slots and return immediately
        if not program and not major:
            dispatcher.utter_message(text="Which program type and major are you interested in? (e.g., Associate or Bachelor, Banking Management, FinTech, Accounting)")
            return []
        if not program:
            dispatcher.utter_message(text="Which program type are you interested in? (Associate, Bachelor)")
            return []
        if not major:
            dispatcher.utter_message(text="Which major are you interested in? (Banking Management, FinTech, Accounting)")
            return []

        # Only give details if both slots are present
        if program.lower() in ["associate", "bachelor"] and major.lower() == "banking management":
            if program.lower() == "associate":
                details = (
                    "**Associate Degree in Banking Management**\n\n"
                    "*Year 1 Semester 1:*\n"
                    "- Principles of Accounting (3 credits)\n"
                    "- Principles of Money and Banking (3)\n"
                    "- Principles of Microeconomics (3)\n"
                    "- Mathematics for Finance (3)\n"
                    "- English for Communication (2)\n"
                    "- Foundation of Digital Productivity (2)\n"
                    "- History (1)\n\n"
                    "*Year 1 Semester 2:*\n"
                    "- Financial Accounting (3)\n"
                    "- Banking Products & Ethics of Sales (2)\n"
                    "- Principles of Macroeconomics (3)\n"
                    "- Advanced Mathematics for Finance (3)\n"
                    "- English for Banking (2)\n"
                    "- Philosophy (1)\n"
                    "- Introduction to Banking Laws (2)\n\n"
                    "*Year 2 Semester 1:*\n"
                    "- Applied Accounting and Banking Operation (3)\n"
                    "- Financial Analysis (3)\n"
                    "- Insurance (2)\n"
                    "- Introduction to Financial Markets (2)\n"
                    "- Responsible Banking (CBI BAF_2036) (2)\n"
                    "- Corporate Banking: Large Corp. & SME Lending (2)\n"
                    "- Wealth & Asset Management (2)\n"
                    "- Company Law (2)\n"
                    "- English for Academic (2)\n\n"
                    "*Year 2 Semester 2:*\n"
                    "- Statistics for Economics and Business (3)\n"
                    "- Introduction to FX & ALM (2)\n"
                    "- Microfinance & Financial Inclusion (2)\n"
                    "- Real Estate Finance (2)\n"
                    "- Sustainable Banking (CBI BAF_2045) (2)\n"
                    "- Digital Banking & Fintech (2)\n"
                    "- Monetary Economics (2)\n"
                    "- Contract Law (2)\n"
                    "- Digital Transformation Banking (2)\n"
                )
            else:  # bachelor
                details = (
                    "**Bachelor Degree in Banking Management**\n\n"
                    "*Year 3 Semester 1:*\n"
                    "- International Economics (2)\n"
                    "- Central Banking, Monetary Policy & Financial Stability (3)\n"
                    "- Programming for Banking and Financial (2)\n"
                    "- ACCA (to be defined) (2)\n"
                    "- Audit & Risk Management (2)\n"
                    "- Commercial & Corporate Lending (CBI BAF_3052) (2)\n"
                    "- FinTech Law (2)\n"
                    "- English for Banking Advanced (1)\n\n"
                    "*Year 3 Semester 2:*\n"
                    "- Industrial Economics (2)\n"
                    "- Data Analytics for Banking and Financial (2)\n"
                    "- ACCA (to be defined) (2)\n"
                    "- Financial Management & Corporate Valuation (3)\n"
                    "- Management & Organization (2)\n"
                    "- Digital & AI Evolution in Banking (CBI) (2)\n"
                    "- Consumer Protection Law I (2)\n"
                    "- English for Academics Advanced (1)\n\n"
                    "*Year 4 Semester 1:*\n"
                    "- ACCA (to be defined) (2)\n"
                    "- Consumer Protection Law II (2)\n"
                    "- Marketing in the Financial Sector (2)\n"
                    "- SME Lending (IBF BAF_4076) (2)\n"
                    "- Trade Finance & Cash Management (2)\n"
                    "- Risk Management in Banking (IBF BAF_4075) (2)\n"
                    "- Strategy in the Financial Sector (2)\n"
                    "- Combating Illicit Finance (2)\n"
                    "- Research Methodology & Ethics (2)\n\n"
                    "*Year 4 Semester 2:*\n"
                    "- Cost Accounting & Management Control (2)\n"
                    "- Compliance & Internal Audit (IBF BAF_4087) (2)\n"
                    "- Advanced Financial Markets (2)\n"
                    "- Academic Thesis / Internship (BAF_4086) (3)\n"
                    "- Green Transition Finance (2)\n"
                    "- CSR, Business Ethics & Investor Relations (2)\n"
                    "- Human Resource Management (2)\n"
                    "- Project Management & Business Simulation (2)\n"
                    "- ACCA (to be defined) (2)\n"
                    "- English Advanced Track / Chinese Basic & Intermediate (1)\n"
                )
            dispatcher.utter_message(text=details)
            # Reset slots after answer
            return [SlotSet("program_type", None), SlotSet("major", None)]

        # If both slots are present but not a supported combination
        dispatcher.utter_message(text=f"Sorry, I only have detailed course information for Banking Management in Associate or Bachelor programs.")
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

