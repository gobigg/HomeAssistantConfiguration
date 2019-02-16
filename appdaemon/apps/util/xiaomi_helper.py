import appdaemon.plugins.hass.hassapi as hass
import datetime
from datetime import datetime

class XiaomiHelper(hass.Hass):
    def initialize(self) -> None:

        self.listen_event(self.event_received, entity_id = "binary_sensor.dryer_vib")

    def event_received(self, event_name, data, kwargs):
        # event_data = data["movement_type"]
        # event_id = data["id"]
        # event_received = datetime.now()

        self.log("Xiaomi data: {}".format(data))
        # self.set_state("sensor.vib_event", state = event_id, attributes = {"event_data": event_data, "event_received": str(event_received)})