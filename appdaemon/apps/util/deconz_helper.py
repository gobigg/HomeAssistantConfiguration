import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime, date

class DeconzHelper(hass.Hass):
    def initialize(self) -> None:
        self.listen_event(self.event_received, "deconz_event")
        self.listen_event(self.vibration_event, "deconz_event", id = "vibration")
        self.handle = None

    def event_received(self, event_name, data, kwargs):
        event_data = data["event"]
        event_id = data["id"]
        event_received = datetime.now()

        self.log("Deconz event received from {}. Event was: {}".format(event_id, event_data))
        self.set_state("sensor.deconz_event", state = event_id, attributes = {"event_data": event_data, "event_received": str(event_received)})
    
    def vibration_event(self, event_name, data, kwargs):
        event_data = data["event"]
        event_id = data["id"]
        event_received_date = datetime.now().date()
        event_received_time = datetime.now().time()

        self.log("Vibration event received. Event was: {}".format(event_data))
        self.set_state("sensor.vibration", state = event_data, attributes = {"event_received_time": str(event_received_time),"event_received_date": str(event_received_date)})
        self.cancel_timer(self.handle)
        
        self.handle = self.run_in(self.cancel_event, 5)
    
    def cancel_event(self, kwargs):
        event_received_date = datetime.now().date()
        event_received_time = datetime.now().time()
        self.set_state("sensor.vibration", state = "0", attributes = {"event_received_time": str(event_received_time),"event_received_date": str(event_received_date)})