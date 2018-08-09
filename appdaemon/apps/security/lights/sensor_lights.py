import appdaemon.plugins.hass.hassapi as hass

#
# App to turn lights on when motion detected then off again after a delay
#
# Use with constrints to activate only for the hours of darkness
#
# Args:
#
# sensor: binary sensor to use as trigger
# entity_on : entity to turn on when detecting motion, can be a light, script, scene or anything else that can be turned on
# entity_off : entity to turn off when detecting motion, can be a light, script or anything else that can be turned off. Can also be a scene which will be turned on
# delay: amount of time after turning on to turn off again. If not specified defaults to 60 seconds.
#
# Release Notes
#
# Version 1.1:
#   Add ability for other apps to cancel the timer
#
# Version 1.0:
#   Initial Version

class SensorLights(hass.Hass):

  def initialize(self):
    
    self.handle = None
    
    # Check some Params

    # Subscribe to sensors
    if "sensor" in self.args:
      for sensor in self.split_device_list(self.args["sensor"]):
        self.listen_state(self.motion, sensor)
    else:
      self.log("No sensor specified, doing nothing")
    
  def motion(self, entity, attribute, old, new, kwargs):
    if new == "on":
        if "entity_on" in self.args:
          for entity_on in self.split_device_list(self.args["entity_on"]):
            self.log("Motion detected: turning {} on".format(entity_on))
            self.turn_on(entity_on)
        if "delay" in self.args:
          delay = self.args["delay"]
        else:
          delay = 300
        self.cancel_timer(self.handle)
        self.handle = self.run_in(self.light_off, delay)
  
  def light_off(self, kwargs):
    if "entity_off" in self.args:
      for entity_off in self.split_device_list(self.args["entity_off"]):
        self.log("Turning {} off".format(entity_off))
        self.turn_off(entity_off)
        
  def cancel(self):
    self.cancel_timer(self.handle)