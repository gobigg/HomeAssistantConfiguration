import appdaemon.plugins.hass.hassapi as hass
import datetime
import time
import globals

class Mailbox(hass.Hass):

    def initialize(self):


        self.door_sensor = self.args["door_sensor"]
        self.slot_sensor = self.args["slot_sensor"]
        self.mail_sensor = self.args["mail_sensor"]
        self.state = self.get_state(self.mail_sensor)
        self.newState = ""
        self.attributes = {}      
        self.just_opened_door = False
        
        self.listen_state(self.just_opened, "sensor.front_door_access_control")
        self.listen_event(self.make_sensor, "plugin_started")

        if "slot_sensor" in self.args:
            self.listen_state(self.mailbox_opened, self.slot_sensor)
        if "door_sensor" in self.args:
            self.listen_state(self.mailbox_opened, self.door_sensor)
 
    def just_opened(self, entity, attribute, old, new, kwargs):
            self.log("Just opened front door")
            self.just_opened_door = True
            self.run_in(self.reset_just_opened, 90)

    def reset_just_opened():
        self.log("Front door no longer just opened")
        self.just_opened_door = False
            

    def mailbox_opened(self, entity, attribute, old, new, kwargs):
        self.state = self.get_state(self.mail_sensor)
        if (new == "on"):
            self.log("Mailbox opened")
            if (entity == self.slot_sensor):
                if (self.state == "Mail" or self.state == "Empty"):
                    self.newState = "Mail"
                    self.log("Mail. Old state: {} - New state: {}".format(self.state, self.newState))
                else:
                    self.newState = "Package and mail"
                    self.log("Mail. Old state: {} - New state: {}".format(self.state, self.newState))

                if (self.state != self.newState):
                    self.call_service("notify/ios_isabellas_iphone_x", message = "You've got {}".format(self.newState))

                self.attributes['icon'] = "mdi:mailbox"
                self.attributes['latest_emptied'] = self.get_state(self.mail_sensor, attribute="latest_emptied")
                self.attributes['latest_mail']=local_time_str(datetime.datetime.now(datetime.timezone.utc))
                self.set_state(self.mail_sensor, state=self.newState, attributes=self.attributes)

            elif (entity == self.door_sensor):
                self.package_or_emptied(entity, old, new)


    def package_or_emptied(self, entity, old, new):
        if (entity == self.door_sensor):
            isa = self.get_state("sensor.presence_isa")
            stefan = self.get_state("sensor.presence_stefan")

            if (self.just_opened_door or isa == "Just arrived" or stefan == "Just arrived"):
                self.mailbox_emptied()
            else:
                self.new_package()
        
    def mailbox_emptied(self):
        self.call_service("notify/ios_isabellas_iphone_x", message = "Mailbox emptied")
            
        self.attributes['icon'] = "mdi:dots-horizontal"
        self.attributes['latest_emptied'] = local_time_str(datetime.datetime.now(datetime.timezone.utc))
        self.attributes['latest_mail']=self.get_state(self.mail_sensor, attribute="latest_mail")
        self.set_state(self.mail_sensor, state=self.newState, attributes=self.attributes)
        self.log("Mailbox emptied")
    
    def new_package(self):
        if (self.state == "Package" or self.state == "Empty"):
            self.newState = "Package"
            self.log("Package. Old state: {} - New state: {}".format(self.state, self.newState))
        else:
            self.newState = "Package and mail"
            self.log("Package. Old state: {} - New state: {}".format(self.state, self.newState))
            
        if (self.state != self.newState):
            self.call_service("notify/ios_isabellas_iphone_x", message = "You've got {}".format(self.newState))
            
        self.attributes['icon'] = "mdi:mailbox"
        # self.attributes['latest_emptied'] = local_time_str(datetime.datetime.now(datetime.timezone.utc))
        self.attributes['latest_emptied'] = self.get_state(self.mail_sensor, attribute="latest_emptied")
        self.attributes['latest_mail']=local_time_str(datetime.datetime.now(datetime.timezone.utc))
        self.set_state(self.mail_sensor, state=self.newState, attributes=self.attributes)
        self.log("Check mail")
    
    def make_sensor(self, event_name, data, kwargs):
        attributes = {}       
        attributes['icon'] = "mdi:dots-horizontal"
        attributes['latest_emptied'] = None
        attributes['latest_mail'] = None
        self.set_state(self.mail_sensor, state="Empty", attributes=attributes)

    def local_time_str(self, utc_datetime):
        now_timestamp = time.time()
        offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
        local_datetime = utc_datetime + offset
        return local_datetime.strftime("%Y-%m-%d %H:%M")