from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import datetime, date


class Dryer(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.handle = None
        self.vibration_sensor = self.args["vibration_sensor"]
        self.dryer_state = self.args["input_select"]
        # self.hatch = self.args["dryer_hatch_sensor"]

        self.listen_event(self.vibration_event, "deconz_event", id = "dryer")
    #     self.light = self.args["light"]
    #     self.light_state = None

    #     self.reminder_handle = None

    #     self.listen_state(self.dryer_running, self.vibration_sensor, new = "False", duration = 90)
    #     self.listen_state(self.washer_clean, self.vibration_sensor, new = "True", duration = 270)
    #     # self.listen_state(self.washer_emptied, self.hatch, new = "on")

    #     self.listen_event(self.snooze_reminder, "ios.notification_action_fired", actionName = "WASHER_NOT_EMPTIED")


    def vibration_event(self, event_name, data, kwargs):
        event_data = data["event"]
        event_id = data["id"]
        event_received_date = datetime.now().date()
        event_received_time = datetime.now().time()

        self.log("Vibration event received. Event was: {}".format(event_data))
        self.set_state("sensor.vibration", state = event_data, attributes = {"event_received_time": str(event_received_time),"event_received_date": str(event_received_date)})
        self.cancel_timer(self.handle)
        
        self.handle = self.run_in(self.cancel_event, 90)
    
    def cancel_event(self, kwargs):
        event_received_date = datetime.now().date()
        event_received_time = datetime.now().time()
        self.set_state("sensor.vibration", state = "0", attributes = {"event_received_time": str(event_received_time),"event_received_date": str(event_received_date)})


    # def dryer_running(self, entity, attribute, new, old, kwargs):
    #     if new != old:
    #         self.select_option(self.washer_state, "Running")
    #         self.log("Washer running")
    #         self.notification_manager.log_home(message = "Washer running.")
    
    # def washer_clean(self, entity, attribute, new, old, kwargs):
    #     if new != old and self.get_state(self.washer_state) == "Running":
    #         self.select_option(self.washer_state, "Clean")
    #         self.log("Washer clean")
    #         self.notification_manager.log_home(message = "Washer clean.")

    #         self.light_state = self.get_state(self.light, attribute = "all")
    #         self.turn_on(self.light, color_name = "red")

    #         self.data = {"push": {"category":"washer", "thread-id":"home-assistant"}}
    #         self.notification_manager.notify_if_home(person = "Isa", message = "Washing machine is done", data = self.data)

    # def washer_emptied(self, entity, attribute, new, old, kwargs):
    #     if new != old and self.get_state(self.washer_state) == "Clean":
    #         self.select_option(self.washer_state, "Idle")
    #         self.log("Washer emptied, now idle")

    #         if self.reminder_handle is not None:
    #             self.cancel_timer(self.reminder_handle)
    #             self.reminder_handle = None

    #         if self.light_state["state"] == "off":
    #             self.turn_on(self.light, color_temp = 366)
    #             self.turn_off(self.light)
    #             self.notification_manager.log_home(message = "Washer emptied, now idle. Turning off lamp.")

    #         else:
    #             brightness = self.light_state["attributes"]["brightness"]
    #             color_temp = self.light_state["attributes"]["color_temp"]
    #             self.turn_on(self.light, color_temp = color_temp, brightness = brightness)
    #             self.notification_manager.log_home(message = "Washer emptied, now idle. Returning lamp to previous state.")

    # def snooze_reminder(self, event_name, data, kwargs):
    #     self.reminder_handle = self.run_in(self.remind_again, 1800)
    
    # def remind_again(self):
    #     self.data = {"push": {"category":"washer", "thread-id":"home-assistant"}}
    #     self.notification_manager.notify_if_home(person = "Isa", message = "Washing machine is done", data = self.data)
