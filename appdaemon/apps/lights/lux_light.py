from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date

class LuxLight(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.light = self.args["light"]
        self.sensor = self.args["sensor"]

        self.listen_state(self.lux_light, self.sensor)

    def lux_light(self, entity, attribute, new, old, kwargs):
        if float(new) < 20 and self.presence_helper.anyone_home() and not self.now_is_between("21:00:00", "11:00:00"):
            if self.get_state(self.light) is "off":
                self.turn_on(self.light, transition = 60, brightness_pct = 25)
                self.log("Turned on {}".format(self.light))