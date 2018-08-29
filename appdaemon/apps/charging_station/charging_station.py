from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime


class ChargingStation(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.plug = "switch.bike_plug_switch"
        self.power_sensor_idle = "sensor.ebike_charger"
        self.isa = PEOPLE['Isa']['device_tracker']

        self.reminder_handle = None
        self.start_quiet = globals.notification_mode["start_quiet_weekday"]
        self.stop_quiet = globals.notification_mode["stop_quiet_weekday"]

        self.listen_state(self.coming_home, self.isa, new = "Just arrived")
        self.listen_state(self.turn_off_charger, self.power_sensor_idle, new = "True")

    def coming_home(self, entity, attribute, new, old, kwargs):
        if(new != old):
            self.run_in(self.turn_on_charger, 5400)        

    def turn_on_charger(self, kwargs):
        self.turn_on(self.plug)
        self.log("Ebike charger turned on")
        reminder_start = self.datetime()
        if (self.reminder_handle is not None):
            return
        else:
            self.reminder_handle = self.run_every(self.check_charge, reminder_start, 1800)
    
    def check_charge(self, kwargs):
        self.log("Checking charge")
        if (self.get_state(self.power_sensor_idle) == "True"):
            if (self.now_is_between(self.stop_quiet, self.start_quiet)):
                self.log("Reminding to charge ebike battery")
                self.call_service(globals.notify_ios_isa, message = "Charge ebike battery!")
        else:
            self.log("Reminder canceled")
            self.cancel_timer(self.reminder_handle)
            self.reminder_handle = None

    def turn_off_charger(self, entity, attribute, new, old, kwargs):
        if (new != old):
            self.log("Fully charged, turning off plug")
            self.turn_off(self.plug)
            self.call_service(globals.notify_ios_isa, title = "Ebike plug turned off", message = "Battery fully charged")