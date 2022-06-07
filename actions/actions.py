# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet, AllSlotsReset
from rasa_sdk import Tracker, FormValidationAction, Action

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from send_request import send_request_with_message
from inventery import update_count, get_count
from connectDB import connect_db, store_in_preson_issue
from dateApi import get_time


class ResetSlots(Action):

    def name(self):
        return "action_reset_slots"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        return [AllSlotsReset()]


class ResponseToRoom(FormValidationAction):

    def name(self) -> Text:
        return "validate_action_comfirm_form"

    def validate_room_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        room = next(tracker.get_latest_entity_values("room_number"), None)

        if (room is None) or len(slot_value) > 3:

            msg = f"Please enter room number in 3 digits"
            dispatcher.utter_message(text=msg)
            return {"room_number": None}

        date = get_time()
        conn = connect_db()
        store_in_preson_issue(conn, date, slot_value)
        room = str(slot_value)
        msg = f"You have entered Room: {room}"
        title = f"Need In Preson Support at Room {slot_value}"
        message = f"Please reply ASPS. Date: {date}"
        send_request_with_message(
            "sjsujackdummy@gmail.com", "sjsujackdummy@gmail.com", title, message)
        dispatcher.utter_message(text=msg)
        return {"room_number": slot_value}


device_dict = ["headphone", "ipad", "macbook",
               "headphones", "ipads", "macbooks"]


class ResponseToDeviceForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_action_device_form"

    def validate_device(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        device = next(tracker.get_latest_entity_values("device"), None)

        if (device is None) or (slot_value.lower() not in device_dict):
            dispatcher.utter_message(
                response="utter_device")
            return {"device": None}
        count = next(tracker.get_latest_entity_values("device_number"), None)
        # print("count")
        # print(count)
        if not count:
            dispatcher.utter_message(
                response="utter_device_number")
            return {"device": slot_value}

        count = int(count)

        inv_device_count = get_count(slot_value)
        if count > inv_device_count:
            dispatcher.utter_message(
                text=f"We only have {inv_device_count} {slot_value} left in our inventery, We will left you know once we have more")
            update_count(slot_value, inv_device_count)
            SlotSet("device_number", str(inv_device_count))
        else:
            dispatcher.utter_message(
                text=f"You can stop by our IT Office for picking up your devices.")
            update_count(slot_value, count)

        return {"device": slot_value}

    def validate_device_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        device = tracker.get_slot("device")
        # print("device")
        # print(device)
        if not device:
            dispatcher.utter_message(response="utter_device")
            return {"device_number": slot_value}

        if len(slot_value) > 2 or int(slot_value) > 10:
            dispatcher.utter_message(
                text=f"Please contact our IT support at IT@sjsu.edu if you need more than 100 devices")
            return {"device_number": None}

        update_count(device, int(slot_value))
        return {"device_number": slot_value}
