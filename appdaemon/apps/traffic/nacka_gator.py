from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date, datetime

class NackaGator(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.listen_state(self.sort_new_tweet, "sensor.nacka_gator_tweet")

    def sort_new_tweet(self, entity, attribute, old, new, kwargs):
        if new != old:
            if "cyk" in new.lower():
                event_received_date = datetime.now().date()
                event_received_time = datetime.now().time()
                self.set_state("sensor.bike_tweet", state = new, attributes = {"event_received_time": str(event_received_time)[:5],"event_received_date": str(event_received_date)})
                self.notification_manager.log_home(message = f"Updated bike tweet: {new}")
                self.log("Updated bike tweet")