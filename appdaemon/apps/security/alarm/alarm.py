from base import Base
import globals
from globals import HouseModes, PEOPLE

class Alarm(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.alarm = self.args["alarm"]
        self.code = self.args["alarm_code"]

        self.listen_state(self.notify_state, self.alarm)
        self.listen_event(self.lights_off_away, "ios.notification_action_fired", actionName = "LIGHTS_OFF")

        if "devices" in self.args:
            for device in self.split_device_list(self.args["devices"]):
                self.listen_state(self.arm_or_disarm, device)

    def arm_or_disarm(self, entity, attribute, old, new, kwargs):
        if new != old and new != None and old != None:
            self.log("Alarm state: {}".format(self.get_state(self.alarm)))
            if self.presence_helper.anyone_just_arrived():
                self.notification_manager.log_alarm(message = "Someone just got home.")
                self.disarm(entity, old, new)
            elif not self.presence_helper.anyone_home():
                self.notification_manager.log_alarm(message = "No one is home.")
                
                if self.get_state("calendar.cleaning_day") == 'on':
                    self.arm_home(entity, old, new)
                else:
                    self.arm_away(entity, old, new)
                
    def arm_away(self, entity, old, new):
        if new != "Just left":
            self.log("Attempting to arm away")
            alarm_state = self.get_state(self.alarm)
            if alarm_state != "armed_away"  and alarm_state != "pending":
                if alarm_state != "disarmed":
                    self.notification_manager.log_alarm(message = "Disarming alarm before arming.")
                    self.call_service("alarm_control_panel/alarm_disarm", entity_id = self.alarm, code = self.code)
                self.call_service("alarm_control_panel/alarm_arm_away", entity_id = self.alarm, code = self.code)
                self.log("Alarm arming")
                self.notification_manager.log_alarm(message = "Arming away.")
            else:
                self.log("Alarm already armed for away")
                self.notification_manager.log_alarm(message = "Alarm already armed for away.")

    def arm_home(self, entity, old, new):
        self.log("Attempting to arm home")
        alarm_state = self.get_state(self.alarm)
        if alarm_state != "armed_home"  and alarm_state != "pending":
            if alarm_state != "disarmed":
                self.notification_manager.log_alarm(message = "Disarming alarm before arming.")
                self.call_service("alarm_control_panel/alarm_disarm", entity_id = self.alarm, code = self.code)
            self.log("Arming home")
            self.call_service("alarm_control_panel/alarm_arm_home", entity_id = self.alarm, code = self.code)
        else:
            self.log("Alarm already armed for home")

    def arm_perimeter(self, entity, old, new): 
        self.log("Attempting to arm perimeter")
        if self.get_state(self.alarm) != "armed_perimeter": 
            self.log("Arming perimeter")
            self.call_service("alarm_control_panel/alarm_arm_night", entity_id = self.alarm, code = self.code)
        else:
            self.log("Alarm already armed for perimeter")

    def disarm(self, entity, old, new):
        self.log("Attempting to disarm alarm")
        if self.get_state(self.alarm) != "disarmed":
            self.log("Disarming alarm")
            self.call_service("alarm_control_panel/alarm_disarm", entity_id = self.alarm, code = self.code)
        else:
            self.log("Alarm already disarmed")

    def notify_state(self, entity, attribute, old, new, kwargs):
        if new != old and new != None:
            if new == "armed_away":
                self.log("Armed away")
                if self.get_state("light.lights_automation") == "on":
                    self.data = {"push": {"category":"lights_off_away", "thread-id":"alarm_control_panel.house"}}
                    self.notify("Do you want to turn off lights?", title = "Alarm armed away", name = PEOPLE["Isa"]['notifier'], data = self.data)
                    self.notification_manager.log_alarm(message = "Alarm armed away. Asking to turn off lights.")
                else:
                    self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                    self.notify("Good bye!", title = "Alarm armed away", name = PEOPLE["Isa"]['notifier'], data = self.data)
                    self.notification_manager.log_alarm(message = "Alarm armed away. All lights already off.")
            elif new == "triggered":
                trigger = self.get_state(self.alarm, attribute = "changed_by")
                trigger_name = self.get_state(trigger, attribute = "friendly_name")
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(trigger_name, title = "ALARM TRIGGERED!", name = PEOPLE["Isa"]['notifier'], data = self.data)
                self.notification_manager.log_alarm(message = f"@here Alarm triggered by {trigger_name}.")
                
                self.beta_data = {"push":{"sound": {"critical": 1, "name": "default", "volume": 0.0 },"category": "alarm", "thread-id": "alarm_control_panel.house"}}    
                self.notify(trigger_name, title = "ALARM TRIGGERED!", name = 'ios_isabellas_iphone_x_beta', data = self.beta_data)

            elif new == "warning":
                trigger = self.get_state(self.alarm, attribute = "changed_by")
                trigger_name = self.get_state(trigger, attribute = "friendly_name")
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(trigger_name, title = "ALARM warning!", name = PEOPLE["Isa"]['notifier'], data = self.data)
            
            else:
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(new, title = "Alarm", name = PEOPLE["Isa"]['notifier'], data = self.data)
                self.notification_manager.log_alarm(message = f"Alarm {new}")

    def lights_off_away(self, event_name, data, kwargs):
        if not self.presence_helper.anyone_home():
            self.turn_off("light.lights_automation")
            self.log("Lights turned off")
            self.notification_manager.log_alarm(message = "Lights turned off after arming away.")
        else:
            self.log("Lights stays on, someone is home.")
            self.notification_manager.log_alarm(message = "Someone is home. Lights stay on.")