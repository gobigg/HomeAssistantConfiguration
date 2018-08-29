from base import Base
from globals import HouseModes, PEOPLE
import globals


"""
    Creates a group with devices with battery below specified limit
"""


class CleaningDay(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.cleaning_calendar = "calendar.cleaning_day"
        self.cleaning_day = "input_boolean.cleaning_day"

        self.listen_state(self.cleaning_day_on_off, self.cleaning_calendar)
    
    def cleaning_day_on_off(self, entity, attribute, new, old, kwargs):
        if (new == "on"):
            self.log("Cleaning day turned on")
            self.turn_on(self.cleaning_day)
        elif (new == "off"):
            self.log("Cleaning day turned off")
            self.turn_off(self.cleaning_day)