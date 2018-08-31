from base import Base

class TTSManager(Base):

    def initialize(self) -> None:
        """Initialize."""
        super().initialize() # Always call base class

    def notify_if_home(self, person:str, title:str, message:str, during_quiet:bool **kwargs:dict) -> None:
        if self.get_state(PEOPLE[person]['device_tracker']) == "Home":
            if during_quiet is False:
                if not quiet_time():
                    self.call_service(PEOPLE[person]['notifier'], title = title, message = message)
        
        PEOPLE[person]['device_tracker']

    def quiet_time(self) -> bool:
        if self.get_state("binary_sensor.workday_sensor") == "on":
            return self.now_is_between(globals.notification_mode["start_quiet_weekday"], globals.notification_mode["stop_quiet_weekday"])
        else
            return self.now_is_between(globals.notification_mode["start_quiet_weekend"], globals.notification_mode["stop_quiet_weekend"])
