from base import Base
from globals import HouseModes, PEOPLE
import globals
import datetime
from datetime import timedelta, date
import json

class Todoist(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()
        
        self.project = self.args['project']
        self.event_boolean = "input_boolean.{}".format(self.args["calendar_boolean_name"])
        self.days_until_next = int(self.args["days_until_next"])

        self.listen_state(self.schedule_next_event, self.event_boolean, new = "off")
        # self.listen_state(self.remind_todo, self.event_boolean, new = "on")
        self.listen_state()
        
    def schedule_next_event(self, entity, attribute, new, old, kwargs):
        due_date = date.today() + timedelta(days=self.days_until_next)
        task = self.get_state(entity = entity, attribute="friendly_name")

        self.call_service("calendar/todoist_new_task", content = task, project = self.project, due_date = str(due_date))
        self.log("Event {} created in Todoist on {}".format(task, str(due_date)))