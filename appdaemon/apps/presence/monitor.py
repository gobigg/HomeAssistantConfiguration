import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
import globals
from globals import PEOPLE
from base import Base
import json

class Monitor(Base):
    
    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.listen_state(self.trigger_departure_scan, "binary_sensor.yard_door")
        self.listen_state(self.trigger_departure_scan, "sensor.front_door_access_control")
    #     self.listen_event(self.event_listener, 'HASS_MQTT_PRESENCE')

    # def event_listener(self, event_name, data, *args, **kwargs):
    #     topic = data['topic'] if data.get('topic') else {}
    #     self.log(topic)
    #     if self.args["DeviceMAC"] in topic:
    #         payload = json.loads(data['payload']) if data.get('payload') else {}
    #         confidence = payload.get('confidence')
    #         if confidence == "100":
    #             self.log("{} spotted!".format(self.args["DeviceID"]))
    #         else:
    #             self.log("{} not found".format(self.args["DeviceID"]))

    def trigger_departure_scan(self, entity, attribute, old, new, kwargs):
        if new == "22" or new == "on":
            self.log("Initiating departure scan in 30 sec")

            self.run_in(self.scan, 30)
            self.run_in(self.scan, 60)
            self.run_in(self.scan, 90)
            self.log("Last departure scan in 30 sec")
            self.run_in(self.scan, 120)

    def scan(self, kwargs):
        self.log("Scanning...")
        self.call_service("mqtt/publish", topic = "monitor/scan/depart")

class MonitorStatus(Base):
    
    def initialize(self) -> None:
        """Initialize."""
        super().initialize()

        self.listen_state(self.monitor_status, "sensor.monitor")

    def monitor_status(self, entity, attribute, old, new, kwargs):
        if new != old:
            self.call_service("notify/ios_isabellas_iphone_x", message = f"Monitor is {new}")