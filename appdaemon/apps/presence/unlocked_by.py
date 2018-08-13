import appdaemon.plugins.hass.hassapi as hass
import datetime
import globals

class UnlockedBy(hass.Hass):

    def initialize(self):
        if "unlocked_by" in self.args:
            self.listen_state(self.set_tracker, self.args["unlocked_by"])

    def set_tracker(self, entity, attribute, old, new, kwargs):
        attributes = {}
        attributes['source_type'] = "lock"
        lock = self.get_state(entity=self.args["unlocked_by"], attribute="all")
        i = datetime.datetime.now()
        now = i.strftime('%Y-%m-%d %H.%M.%S')
        if (new == 'Stefan'):
            device = self.get_state(entity=self.args["stefan"], attribute="all")
            deviceState = self.get_state(self.args["stefan"])
            attributes["lock_last_updated"]=now
            if (deviceState != 'Home'):
                self.set_state(self.args["stefan"], state='Home', attributes=attributes)
        if (new == 'Isabella'):
            device = self.get_state(entity=self.args["isa"], attribute="all")
            deviceState = self.get_state(self.args["isa"])
            attributes["lock_last_updated"]=now
            if (deviceState != 'Home'):
                self.set_state(self.args["isa"], state='Home', attributes=attributes)
