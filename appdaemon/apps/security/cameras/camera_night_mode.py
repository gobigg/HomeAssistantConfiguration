from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date

class CameraNightMode(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.run_at_sunset(self.night_mode_on)

        self.run_at_sunrise(self.night_mode_off)

    def night_mode_on(self, kwargs):
        self.turn_on_device("switch.dafang_night_mode")
        self.log("Turned on night mode for cameras")
        self.notification_manager.log_home(message = "Turned on night mode for cameras.")
    
    def night_mode_off(self, kwargs):
        self.turn_off_device("switch.dafang_night_mode")
        self.log("Turned off night mode for cameras")
        self.notification_manager.log_home(message = "Turned off night mode for cameras.")
