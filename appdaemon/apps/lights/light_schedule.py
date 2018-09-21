from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date

class LightSchedule(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.outdoor_lights = "light.outdoor_lights"
        self.hallway_window = "light.hallway_window_light"
        
        self.lights_at_dark = "scene.lights_at_dark"
        self.dark_lights_off = "script.dark_lights_off"
        self.run_at_sunset(self.lights_on, offset = datetime.timedelta(minutes = -45).total_seconds())
        self.scheduler.run_on_evening_before_weekday(self.lights_out, self.parse_time("23:59:00"))
        self.scheduler.run_on_night_before_weekend_day(self.lights_out, self.parse_time("00:30:00"))

        if (self.sun_down()):
            self.scheduler.run_on_weekdays(self.lights_on, self.parse_time("06:30:00"))
        self.run_at_sunrise(self.lights_out, offset = datetime.timedelta(minutes = 45).total_seconds())

    def lights_on(self, kwargs):
        self.turn_on_device(self.outdoor_lights)
        self.log("Turned on outdoor lights")
    
    def lights_out(self, kwargs):
        self.turn_off_device(self.outdoor_lights)
        self.log("Turned off outdoor lights")