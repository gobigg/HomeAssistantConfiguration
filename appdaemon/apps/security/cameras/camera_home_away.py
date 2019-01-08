from base import Base
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date

class CameraHomeAway(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()
        
        self.alarm = "alarm_control_panel.house"
        self.set_state(self.alarm, state = "disarmed")
        self.listen_state(self.home_away, self.alarm)
        
    def home_away(self, entity, attribute, old, new, kwargs):
        if old != None and old != new:
            if self.get_state(self.alarm) == 'pending':
                self.call_service("script/dafang_calibrate")

            elif self.get_state(self.alarm) == 'disarmed':
                self.notification_manager.log_alarm(message = "Cameras disabled.")
                self.call_service("script/sannce_all_down")
                self.call_service("script/dafang_all_up")
            elif self.get_state(self.alarm) == 'armed_away':
                self.notification_manager.log_alarm(message = "Cameras enabled.")
                self.run_in(self.dafang_away, 21)
                self.run_in(self.dafang_away, 23)
                self.run_in(self.dafang_away, 25)

                self.run_in(self.sannce_away, 60)
                self.run_in(self.sannce_away, 62)
                self.run_in(self.sannce_away, 64)
                self.run_in(self.sannce_away, 66)
                self.run_in(self.sannce_away, 68)
    
    def sannce_away(self, kwargs):
        self.call_service("script/sannce_up")
    
    def dafang_away(self, kwargs):
        self.call_service("script/dafang_down")