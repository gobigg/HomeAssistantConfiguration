import appdaemon.plugins.hass.hassapi as hass
import datetime
import globals

class NotifyRain(hass.Hass):

    def initialize(self):
        self.notified_today = False
        self.rain_percent_today = 0

        self.listen_state(self.rain_today, "sensor.dark_sky_precip_probability")
        self.listen_state(self.rain_tomorrow, "sensor.dark_sky_precip_probability_1")

    def rain_today(self, entity, attribute, old, new, kwargs):
        if (new != old and new != None):
            if (new >= 30 and new > self.rain_percent_today):
                

                self.rain_percent_today = new


            self.call_service(globals.notify_ios_isa, message = "Probability of rain tomorrow is {} %".format(new))