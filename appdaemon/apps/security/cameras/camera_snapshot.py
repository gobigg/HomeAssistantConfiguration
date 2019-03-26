import appdaemon.plugins.hass.hassapi as hass
import datetime
import globals

class CameraMotion(hass.Hass):

  def initialize(self):

    self.camera = self.args["camera"]
    self.url = self.args['url']
    if "sensor" in self.args:
      for sensor in self.split_device_list(self.args["sensor"]):
        self.listen_state(self.motion, sensor)
    # else:
    #   self.listen_state(self.motion, "binary_sensor")
    
  def motion(self, entity, attribute, old, new, kwargs):
    self.log("new: {}".format(new))
    if new == "on" and new != old:
      alarm_state = self.get_state(entity='alarm_control_panel.house')
      if (alarm_state == 'armed_away' or alarm_state == 'armed_night' or alarm_state == 'armed_perimeter' or alarm_state == 'triggered'):
        i = datetime.datetime.now()
        now = i.strftime('%Y-%m-%d %H.%M.%S')
        filenames = "/config/www/motion/{}-{}.jpg".format(now, self.friendly_name(self.camera))
        self.log("Motion detected: {}".format(self.friendly_name(entity)))
        self.call_service("camera/snapshot", entity_id = self.camera, filename = "/config/www/motion/{}_latest.jpg".format(self.friendly_name(self.camera)))
        self.call_service("camera/snapshot", entity_id = self.camera, filename = filenames)

        if (self.get_state(entity='input_boolean.ad_camera_motion_notification') == 'on'):
          data = {"push": {"category": "camera"}, "entity_id": self.camera}
          self.call_service(globals.notify_ios_isa, message = "Motion detected: {}".format(self.friendly_name(entity)), data=data)
          latest_data = {"attachment": {"url":"{}/local/motion/{}_latest.jpg".format(self.url, self.friendly_name(self.camera)), "content-type": "jpg"}}
          self.call_service(globals.notify_ios_isa, message = "Snapshot {}".format(self.friendly_name(self.camera)), data=latest_data)