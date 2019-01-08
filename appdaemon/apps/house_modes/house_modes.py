from base import Base
# from globals import HouseModes, PEOPLE
import globals

class CleaningDay(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()
        self.discord = "notify/hass_discord"
        self.home_channel = "510398531937501186"
        self.cleaning_calendar = "calendar.cleaning_day"
        self.cleaning_day = "input_boolean.cleaning_day"

        # self.set_state(self.cleaning_calendar, state = "on")

        self.listen_state(self.cleaning_day_on, self.cleaning_calendar, new = "on")
        self.listen_state(self.cleaning_day_off, self.cleaning_calendar, new = "off")
    
    def cleaning_day_on(self, entity, attribute, new, old, kwargs):
        self.log("Cleaning day turned on")
        self.call_service(self.discord, target = self.home_channel, message = "Cleaning day turned on")
        self.turn_on(self.cleaning_day)
            
    def cleaning_day_off(self, entity, attribute, new, old, kwargs):
        self.log("Cleaning day turned off")
        self.call_service(self.discord, target = self.home_channel, message = "Cleaning day turned off")
        self.turn_off(self.cleaning_day)
        