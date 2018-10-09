from base import Base
import globals
from globals import HouseModes, PEOPLE

class Alarm(Base):
    def initialize(self):
        """Initialize."""
        super().initialize()

        self.alarm = self.args["alarm"]
        self.code = self.args["alarm_code"]
        # self.set_state("sensor.presence_test", state="Home")

        # self.listen_event(self.keep_state, "plugin_started")
        self.listen_state(self.notify_state, self.alarm)
        self.listen_event(self.lights_off_away, "ios.notification_action_fired", actionName = "LIGHTS_OFF")

        if "devices" in self.args:
            for device in self.split_device_list(self.args["devices"]):
                self.listen_state(self.arm_or_disarm, device)

    def arm_or_disarm(self, entity, attribute, old, new, kwargs):
        if new != old and new != None:
            self.log("Alarm state: {}".format(self.get_state(self.alarm)))
            if self.presence_helper.anyone_just_arrived():
                self.disarm(entity, old, new)
            elif not self.presence_helper.anyone_home():
                self.arm_away(entity, old, new)
                
    def arm_away(self, entity, old, new):
        if new != "Just left":
            self.log("Attempting to arm away")        
            if self.get_state(self.alarm) != "armed_away":
                self.call_service("alarm_control_panel/alarm_arm_away", entity_id = self.alarm, code = self.code)
                self.log("Alarm arming")
            else:
                self.log("Alarm already armed for away")

    def arm_home(self, entity, old, new):
        self.log("Attempting to arm home")        
        if self.get_state(self.alarm) != "armed_home":
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
                if self.get_state("group.inside_lights_automations") == "on":
                    self.data = {"push": {"category":"lights_off_away", "thread-id":"alarm_control_panel.house"}}
                    self.notify("Do you want to turn off lights?", title = "Alarm armed away", name = PEOPLE["Isa"]['notifier'], data = self.data)
                else:
                    self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                    self.notify("Good bye!", title = "Alarm armed away", name = PEOPLE["Isa"]['notifier'], data = self.data)
            elif new == "triggered":
                trigger = self.get_state(self.alarm, attribute = "changed_by")
                trigger_name = self.get_state(trigger, attribute = "friendly_name")
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(trigger_name, title = "ALARM TRIGGERED!", name = PEOPLE["Isa"]['notifier'], data = self.data)

            elif new == "warning":
                trigger = self.get_state(self.alarm, attribute = "changed_by")
                trigger_name = self.get_state(trigger, attribute = "friendly_name")
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(trigger_name, title = "ALARM warning!", name = PEOPLE["Isa"]['notifier'], data = self.data)
            
            else:
                self.data = {"push": { "thread-id":"alarm_control_panel.house"}}
                self.notify(new, title = "Alarm", name = PEOPLE["Isa"]['notifier'], data = self.data)

    def lights_off_away(self, event_name, data, kwargs):
        self.turn_off("group.inside_lights_automations")
        self.log("Lights turned off")