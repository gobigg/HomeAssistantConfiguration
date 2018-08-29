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
        self.start_quiet = globals.notification_mode["start_quiet_weekday"]
        self.stop_quiet = globals.notification_mode["stop_quiet_weekday"]

        self.visits = 0

        self.pause_motion = False

        # self.set_state(self.motion_sensor, state = "off")
        # self.set_state(self.motion_sensor, state = "on")

        self.listen_state(self.count_visit, self.motion_sensor, new = "on")

    def count_visit(self, entity, attribute, new, old, kwargs):
        if (self.pause_motion is False and self.get_state(self.input_select) != "Cleaning"):
            self.call_service("counter/increment", entity_id = self.counter)
            self.call_service("counter/increment", entity_id = self.counter_total)
            self.select_option(self.input_select, "Dirty")

            self.log("Counting up")

            self.pause_motion = True
            self.run_in(self.reset_pause_motion, 180)
            self.visits = int(self.get_state(self.counter))
            if (self.visits >= 2):
                self.send_notification()
            
    def send_notification(self):
        if (self.now_is_between(self.stop_quiet, self.start_quiet)):
            litterbox_name = self.get_state(self.counter, attribute="friendly_name")
            litterbox_name = litterbox_name.replace(" Visits", "")
            litterbox_name = litterbox_name.lower()
            message = "{} visits to {}.".format(self.visits, litterbox_name)

            self.call_service(globals.notify_ios_isa, message = message)
            

    def reset_pause_motion(self, kwargs):
        self.pause_motion = False