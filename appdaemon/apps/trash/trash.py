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
        self.trash_status = "input_boolean.trash_status"
        self.trash = self.get_state("sensor.trash")

        self.attributes = {}

        self.listen_state(self.garbage_day, "calendar.garbage_day")
        self.listen_state(self.take_in_garbage, "calendar.take_in_garbage")
        self.listen_state(self.notify_new_trash_status, "sensor.trash")
        
        # self.init_sensor()

    def notify_new_trash_status(self, entity, attribute, old, new, kwargs):
        if new != old:
            self.notification_manager.log_home(message = f"Trash can is {new}")

    def garbage_day(self, entity, attribute, old, new, kwargs):
        if new != old and new == "on":
            self.log("It's garbage day")
            self.notification_manager.log_home(message = f"It's garbage day")
            time = datetime.time(0, 0, 0)
            self.put_out_handle = self.run_hourly(self.remind_put_out, time)

    def take_in_garbage(self, entity, attribute, old, new, kwargs):
        if new != old and new == "on":
            self.notification_manager.log_home(message = f"Today we take in the trash can")
            self.log("Time to take in garbage can")
            time = datetime.time(0, 0, 0)
            self.take_in_handle = self.run_hourly(self.remind_take_in, time)

    def remind_put_out(self, kwargs):
        self.trash = self.get_state("sensor.trash")

        if self.trash == "Away":
            self.select_option(self.trash_status, "Out")

            self.cancel_timer(self.put_out_handle)

        elif self.trash == "Home" and self.now_is_between("18:30:00", "23:59:00"):
            self.select_option(self.trash_status, "Put out")

            self.data = {"push": {"thread-id":"trash"}}
            self.notification_manager.notify_if_home(person = "Isa", message = "Put out the trash", data = self.data)
            self.notification_manager.log_home(message = f"Time to put out the trash")

    def remind_take_in(self, kwargs):
        self.trash = self.get_state("sensor.trash")
        if self.trash == "Away" and self.now_is_between("08:30:00", "23:00:00"):
            self.attributes['icon'] = "mdi:delete-empty"
            self.attributes['icon_color'] = "red"
            self.select_option(self.trash_status, "Take in")

            self.data = {"push": {"thread-id":"trash"}}
            self.notification_manager.notify_if_home(person = "Isa", message = "Take in the trash", data = self.data)
            self.notification_manager.log_home(message = f"Take in trash")
            
        elif self.trash == "Home":
            self.attributes['icon'] = "mdi:delete"
            self.attributes['icon_color'] = "white"
            self.select_option(self.trash_status, "Home")

            self.cancel_timer(self.take_in_handle)

    # def init_sensor(self):
    #     self.log("Initializing trash sensor")
    #     if self.trash == 'Away':
    #         if self.get_state("calendar.take_in_garbage") == 'on' or self.get_state("calendar.garbage_day") == 'off':
    #             self.attributes['icon'] = "mdi:delete-empty"
    #             self.attributes['icon_color'] = "red"
    #             self.set_state(self.trash_status, state = "Take in", attributes = self.attributes)
    #         else:
    #             self.attributes['icon'] = "mdi:delete-restore"
    #             self.attributes['icon_color'] = "white"
    #             self.set_state(self.trash_status, state = "Out", attributes = self.attributes)
                
    #     elif self.trash == 'Home':
    #         if self.get_state("calendar.garbage_day") == 'on':
    #             self.attributes['icon'] = "mdi:delete-circle"
    #             self.attributes['icon_color'] = "red"
    #             self.set_state(self.trash_status, state = "Put out", attributes = self.attributes)
    #         else:
    #             self.attributes['icon'] = "mdi:delete"
    #             self.attributes['icon_color'] = "white"
    #             self.set_state(self.trash_status, state = "Home", attributes = self.attributes)