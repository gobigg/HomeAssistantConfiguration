from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, datetime

class LightSchedule(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.lights_at_dark = "scene.lights_at_dark"
        self.dark_lights_off = "script.dark_lights_off"

        """Outdoor and hallway lights evenings"""
        self.run_at_sunset(self.lights_on, offset = datetime.timedelta(minutes = -45).total_seconds())
        self.run_on_evening_before_weekday(self.lights_out, self.parse_time("23:59:59"))
        self.run_on_evening_before_weekend(self.lights_out, self.parse_time("01:00:00")) # fix, now runs on night to friday

        """Outdoor and hallway lights mornings"""       
        if (self.sun_down()):
            self.run_on_weekdays(self.lights_on, self.parse_time("06:30:00"))

        self.run_at_sunrise(self.lights_out, offset = datetime.timedelta(minutes = 45).total_seconds())

    def lights_on(self, kwargs):
        self.turn_on_device(self.lights_at_dark)
        self.log("Turned on lights at sunset")
    
    def lights_out(self, kwargs):
        self.turn_off_device(self.dark_lights_off)
        self.log("Turned off dark lights")