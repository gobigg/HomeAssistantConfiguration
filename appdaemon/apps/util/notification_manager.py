from base import Base
import globals
from globals import PEOPLE

class NotificationManager(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

    """title and during_quiet is optional, default is not during quiet time, use True to override"""
    def notify_if_home(self, person:str, message:str, title:str="", during_quiet:bool=False, **kwargs:dict):
        self.log(self.get_state(PEOPLE[person]['device_tracker']) == "Home")
        if self.get_state(PEOPLE[person]['device_tracker']) == "Home":
            if during_quiet is False:
                if not self.quiet_time():
                    self.log("Sending notification")
                    self.notify(message, title = title, name = PEOPLE[person]['notifier'])
            else:
                self.log("Sending notification")
                self.notify(message, title = title, name = PEOPLE[person]['notifier'])
        
    def quiet_time(self) -> bool:
        if self.get_state("binary_sensor.workday_sensor") == "on":
            return self.now_is_between(globals.notification_mode["start_quiet_weekday"], globals.notification_mode["stop_quiet_weekday"])
        else:
            return self.now_is_between(globals.notification_mode["start_quiet_weekend"], globals.notification_mode["stop_quiet_weekend"])
