from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime


class Laundry(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.power_sensor_idle = self.args["power_sensor"]
        self.washer_state = self.args["input_select"]
        self.hatch = self.args["washer_hatch_sensor"]

        self.light = self.args["light"]
        self.light_state = None

        self.reminder_handle = None

        self.listen_state(self.washer_running, self.power_sensor_idle, new = "False", duration = 90)
        self.listen_state(self.washer_clean, self.power_sensor_idle, new = "True", duration = 270)
        self.listen_state(self.washer_emptied, self.hatch, new = "on")

        self.listen_event(self.snooze_reminder, "ios.notification_action_fired", actionName = "WASHER_NOT_EMPTIED")

    def washer_running(self, entity, attribute, new, old, kwargs):
        if new != old:
            self.select_option(self.washer_state, "Running")
            self.log("Washer running")
    
    def washer_clean(self, entity, attribute, new, old, kwargs):
        if new != old and self.get_state(self.washer_state) == "Running":
            self.select_option(self.washer_state, "Clean")
            self.log("Washer clean")

            self.light_state = self.get_state(self.light, attribute = "all")
            self.turn_on(self.light, color_name = "red")

            self.data = {"push": {"category":"washer", "thread-id":"home-assistant"}}
            self.notification_manager.notify_if_home(person = "Isa", message = "Washing machine is done", data = self.data)

    def washer_emptied(self, entity, attribute, new, old, kwargs):
        if new != old and self.get_state(self.washer_state) == "Clean":
            self.select_option(self.washer_state, "Idle")
            self.log("Washer emptied, now idle")

            if self.reminder_handle is not None:
                self.cancel_timer(self.reminder_handle)
                self.reminder_handle = None

            if self.light_state["state"] == "off":
                self.turn_on(self.light, color_temp = 366)
                self.turn_off(self.light)
            else:
                brightness = self.light_state["attributes"]["brightness"]
                color_temp = self.light_state["attributes"]["color_temp"]
                self.turn_on(self.light, color_temp = color_temp, brightness = brightness)

    def snooze_reminder(self, event_name, data, kwargs):
        self.reminder_handle = self.run_in(self.remind_again, 1800)
    
    def remind_again(self):
        self.data = {"push": {"category":"washer", "thread-id":"home-assistant"}}
        self.notification_manager.notify_if_home(person = "Isa", message = "Washing machine is done", data = self.data)
