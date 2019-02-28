import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime, date
import globals
from globals import PEOPLE

class Rats(hass.Hass):
    def initialize(self) -> None:
        self.listen_event(self.mouse_event, "deconz_event", id = "vibration")
        self.listen_event(self.rat_event, "deconz_event", id = "switch_68")
        self.handle = None


    def mouse_event(self, event_name, data, kwargs):
        self.notify("Mouse vibration triggered", title = "Mouse!", name = PEOPLE['Isa']['notifier'])
        self.notify("Mouse vibration triggered", title = "Mouse!", name = PEOPLE['Stefan']['notifier'])

    def rat_event(self, event_name, data, kwargs):
        self.notify("Rat vibration triggered", title = "Rat!", name = PEOPLE['Isa']['notifier'])
        self.notify("Rat vibration triggered", title = "Rat!", name = PEOPLE['Stefan']['notifier'])
