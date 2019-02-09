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
        self.listen_state(self.bt_change, "sensor.isabellas_iphone_x_bt")
        self.listen_state(self.bt_change, "sensor.stefan_iphone_7_bt")
        self.listen_state(self.monitor_status, "sensor.monitor")
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
    def bt_change(self, entity, attribute, old, new, kwargs):
        if new != old:
            self.notification_manager.log_hass(message = f"Bt tracker change from monitor. {entity} was {old}, now {new}")

    def trigger_departure_scan(self, entity, attribute, old, new, kwargs):
        if new == "22" or new == "on":
            self.log("Initiating departure scan in 30 sec")

            self.run_in(self.scan_depart, 30)
            self.run_in(self.scan_depart, 60)
            self.run_in(self.scan_depart, 90)
            self.log("Last departure scan in 30 sec")
            self.run_in(self.scan_depart, 120)
            isa = self.get_state("sensor.isabellas_iphone_x_bt")
            stefan = self.get_state("sensor.stefan_iphone_7_bt")
            self.notification_manager.log_hass(message = f"Scanned for departure.")

    def monitor_status(self, entity, attribute, old, new, kwargs):
        if new != old:
            # self.call_service("notify/ios_isabellas_iphone_x", message = f"Monitor is {new}")
            self.notification_manager.log_hass(message = f"Monitor is {new}")
            if new == "online":
                self.run_in(self.scan_arrive, 5)
                self.run_in(self.scan_arrive, 30)
                self.run_in(self.scan_arrive, 60)
            
    def scan_arrive(self, kwargs):
        self.log("Scanning for arrival...")
        self.call_service("mqtt/publish", topic = "monitor/scan/arrive")
        
    def scan_depart(self, kwargs):
        self.log("Scanning for departure...")
        self.call_service("mqtt/publish", topic = "monitor/scan/depart")
