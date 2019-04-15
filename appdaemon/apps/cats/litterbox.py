from base import Base
from globals import HouseModes, PEOPLE
import globals
import datetime


class Litterbox(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.motion_sensor = self.args["motion_sensor"]
        self.counter = self.args["counter"]
        self.counter_total = self.args["counter_total"]
        self.input_select = self.args["input_select"]
        self.visits = 0

        self.pause_counter = False

        # self.set_state(self.motion_sensor, state = "off")
        # self.set_state(self.motion_sensor, state = "on")

        self.listen_event(self.button_pressed, "deconz_event", id = self.args["switch"] )
        self.listen_state(self.count_visit, self.motion_sensor, new = "on")

    def count_visit(self, entity, attribute, new, old, kwargs):
        if (self.pause_counter is False and self.get_state(self.input_select) != "Cleaning"):
            self.call_service("counter/increment", entity_id = self.counter)
            self.call_service("counter/increment", entity_id = self.counter_total)
            self.select_option(self.input_select, "Dirty")

            self.log("Counting up")

            self.pause_counter = True
            self.run_in(self.reset_pause_counter, 300)
            self.visits = int(self.get_state(self.counter))
            if (self.visits >= 2):
                self.send_notification()
            
    def send_notification(self):
        litterbox_name = self.get_state(self.counter, attribute="friendly_name")
        litterbox_name = litterbox_name.replace(" Visits", "")
        litterbox_name = litterbox_name.lower()


        message = "{} visits to {}.".format(self.visits, litterbox_name)
        data = {"push": {"thread-id":"litterbox"}}
        # data = {"attachment":{"content-type":"jpeg"},"push": { "category":"camera", "thread-id":"litterbox"},"entity_id":"camera.upstairs"}
        
        self.notification_manager.notify_if_home(person="Isa", message=message, title="Litterbox", data=data)
            
    def button_pressed(self, event_name, data, kwargs):
        self.click_type=data["event"]
        self.log("Button press")
        if self.click_type == 1002:
            self.log("Cleaning")
            self.pause_counter = True
            self.run_in(self.reset_pause_counter, 180)

            self.run_in(self.set_clean, 180)

            self.call_service("counter/reset", entity_id = self.counter)
            self.select_option(self.input_select, "Cleaning")

    def set_clean(self, kwargs):
        self.select_option(self.input_select, "Clean")
        self.log("Clean")


    def reset_pause_counter(self, kwargs):
        self.pause_counter = False