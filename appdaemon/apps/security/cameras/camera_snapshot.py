import appdaemon.plugins.hass.hassapi as hass
import datetime
import globals

class CameraMotion(hass.Hass):

  def initialize(self):
    if "sensor" in self.args:
    #   for sensor in self.split_device_list(self.args["sensor"]):
        self.listen_state(self.motion, self.args["sensor"])
    # else:
    #   self.listen_state(self.motion, "binary_sensor")
    
  def motion(self, entity, attribute, old, new, kwargs):
    if ("state" in new and new["state"] == "on" and old["state"] == "off") or new == "on":
      if (self.get_state(entity='alarm_control_panel.home_alarm') == 'armed_away' or self.get_state(entity='alarm_control_panel.home_alarm') == 'armed_night'):
        i = datetime.datetime.now()
        now = i.strftime('%Y-%m-%d %H.%M.%S')
        filenames = "/config/www/motion/{}-back_door_camera.jpg".format(now)
        self.log("Motion detected: {}".format(self.friendly_name(entity)))
        self.call_service("camera/snapshot", entity_id = "camera.back_door", filename = "/config/www/motion/back_door_camera_latest.jpg")
        self.call_service("camera/snapshot", entity_id = "camera.back_door", filename = filenames)
        # self.notify("Motion detected: {}".format(self.friendly_name(entity)), name=globals.ios_isa)
        if (self.get_state(entity='input_boolean.ad_camera_motion_notification') == 'on'):
          data = {"push": {"category": "camera"}, "entity_id": "camera.latest_motion"}
          self.call_service(globals.notify_ios_isa, message = "Motion detected: {}".format(self.friendly_name(entity)), data=data)