from base import Base
from globals import HouseModes, PEOPLE
import globals
import datetime
from datetime import timedelta, datetime
import json

class Calendar(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.calendar_event = "input_boolean.{}".format(self.args["calendar_boolean_name"])
        self.days_until_next = int(self.args["days_until_next"])

        self.listen_state(self.schedule_next_event, self.calendar_event, new = "off")

    def schedule_next_event(self, entity, attribute, new, old, kwargs):
        date = datetime.now() + timedelta(days=self.days_until_next)
        event_name = self.get_state(entity = entity, attribute="friendly_name")

        # data = "{\"event\":\"make_home_event\",\"value1\":{},\"value2\":{},\"value3\":{}}".format(event_name,str(date),str(date))
        data = "{\"event\":\"make_home_event\"}"
        json_data = json.dumps(data)

        self.call_service("ifttt/trigger", event = event_name, value1 = str(date), value2 = str(date))
        self.log("Event {} created in calendar on {}".format(event_name, str(date)))