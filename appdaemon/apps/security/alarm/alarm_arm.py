import appdaemon.plugins.hass.hassapi as hass
import datetime
import globals

# class AlarmArm(hass.Hass):

#     def initialize(self):
#         if "devices" in self.args:
#             for device in self.split_device_list(self.args["devices"]):
#                 self.listen_state(self.arm_or_disarm, device)

#     def arm_or_disarm(self, entity, attribute, old, new, kwargs):
#         if (new != old and new != None):
#             if (new != "Home" and new != "Just arrived"):
#                 self.arm_away(entity, old, new)
                
#     def arm_away(self, entity, old, new):
#         self.log("arm away")
        
#     def arm_home(self, entity, old, new):
      
#     def arm_night(self, entity, old, new):  
      
#     def disarm(self, entity, old, new):
        
class AlarmKeepState(hass.Hass):
    def initialize(self):
        self.listen_event(self.keep_state, "plugin_started")
        
    def keep_state(self, event_name, data, kwargs):
        self.log("Trying to keep state for alarm")
        isa = self.get_state(globals.isa)
        stefan = self.get_state(globals.stefan)
        if (isa != "Home" and isa != "Just arrived" and stefan != "Home" and stefan != "Just arrived"):
            if (self.get_state("input_boolean.cleaning_day") == "off"):
                self.call_service("alarm_control_panel/alarm_arm_away", entity_id=globals.alarm, code=self.args["alarm_code"])
                self.log("Alarm armed away after restart")
            else:
                self.call_service("alarm_control_panel/alarm_arm_home", entity_id=globals.alarm, code=self.args["alarm_code"])
                self.log("Alarm armed home after restart -> Cleaning day")