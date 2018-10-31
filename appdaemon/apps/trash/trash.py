import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
import globals
from globals import PEOPLE
from base import Base
import json

class Trash(Base):
    
    def initialize(self) -> None:
        """Initialize."""
        super().initialize()
        self.trash = self.get_state("sensor.trash")

        self.attributes = {}

        self.listen_state(self.garbage_day, "calendar.garbage_day")
        self.listen_state(self.take_in_garbage, "calendar.take_in_garbage")

    def garbage_day(self, entity, attribute, old, new, kwargs):
        if new != old and new == "on":
            self.put_out_handle = self.run_hourly(self.remind_put_out, **kwargs)

    def take_in_garbage(self, entity, attribute, old, new, kwargs):
        if new != old and new == "on":
            self.take_in_handle = self.run_hourly(self.remind_take_in, **kwargs)

    def remind_put_out(self, kwargs):
        self.trash = self.get_state("sensor.trash")

        if self.trash == "not_home":
            self.attributes['icon'] = "mdi:delete-restore"
            self.attributes['icon_color'] = "white"
            self.set_state("sensor.trash", state = self.trash, attributes = self.attributes)

            self.cancel_timer(self.put_out_handle)

        elif self.trash == "home" and self.now_is_between("18:30:00", "23:00:00"):
            self.attributes['icon'] = "mdi:delete-circle"
            self.attributes['icon_color'] = "red"
            self.set_state("sensor.trash", state = self.trash, attributes = self.attributes)

            self.data = {"push": {"thread-id":"trash"}}
            self.notification_manager.notify_if_home(person = "Isa", message = "Put out the trash", data = self.data)

    def remind_take_in(self, kwargs):
        self.trash = self.get_state("sensor.trash")
        if self.trash == "not_home" and self.now_is_between("08:30:00", "23:00:00"):
            self.attributes['icon'] = "mdi:delete-empty"
            self.attributes['icon_color'] = "red"
            self.set_state("sensor.trash", state = self.trash, attributes = self.attributes)

            self.data = {"push": {"thread-id":"trash"}}
            self.notification_manager.notify_if_home(person = "Isa", message = "Put out the trash", data = self.data)
        elif self.trash == "home":
            self.attributes['icon'] = "mdi:delete"
            self.attributes['icon_color'] = "white"
            self.set_state("sensor.trash", state = self.trash, attributes = self.attributes)

            self.cancel_timer(self.take_in_handle)
