import appdaemon.plugins.hass.hassapi as hass

class DashboardMotion(hass.Hass):
  handle = None
  isOn = False
  delay = 120 # default delay
  def initialize(self):

    self.handle = None
    # self.set_state("binary_sensor.dashboard_motion", state = "on")
    self.listen_state(self.motion, "binary_sensor.dashboard_motion")

  def motion(self, entity, attribute, old, new, kwargs):
    if new == "on":
      # self.log("Motion detected: turning dashboard on and starting timer for 300 seconds")
      self.call_service("shell_command/dashboard_monitor_on")
      self.isOn = True

      self.cancel_timer(self.handle)
      self.handle = self.run_in(self.dashboard_off, self.delay)

  def dashboard_off(self, kwargs):
    self.log("isOn {}".format(self.isOn))
    if self.isOn:
      # self.log("Turning dashboard off")
      self.call_service("shell_command/dashboard_monitor_off")
      self.isOn = False

  def cancel(self):
    self.cancel_timer(self.handle)