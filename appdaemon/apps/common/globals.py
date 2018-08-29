from enum import Enum

# Global variables

ios_isa = 'ios_isabellas_iphone_x'
notify_ios_isa = "notify/ios_isabellas_iphone_x"

isa = "sensor.presence_isa"
stefan = "sensor.presence_stefan"

alarm = "alarm_control_panel.home_alarm"


notification_mode = {}
notification_mode["start_quiet_weekday"] = "22:00:00"
notification_mode["start_quiet_weekend"] = "23:00:00"
notification_mode["stop_quiet_weekday"] = "07:00:00"
notification_mode["stop_quiet_weekend"] = "09:00:00"


presence_state = {}
# Change this if you want to change the display name
presence_state["home"] = "Home"
presence_state["just_arrived"] = "Just arrived"
presence_state["just_left"] = "Just left"
presence_state["away"] = "Away"
presence_state["extended_away"] = "Extended away"


PEOPLE = {
    'Isa': {
        'device_tracker': 'sensor.presence_isa',
        'proximity': 'proximity.home_isa',
        'notifier': 'ios_isabellas_iphone_x'
    },
    'Stefan': {
        'device_tracker': 'sensor.presence_stefan',
        'proximity': 'proximity.home_stefan'
    }
}

# class GlobalEvents(Enum):
#     # Events
#     # fired when house mode chages, i.e. day, evening, night, morning
#     EV_HOUSE_MODE_CHANGED = 'EV_HOUSE_MODE_CHANGED'
#     # any motion detected in a room
#     EV_MOTION_DETECTED = 'EV_MOTION_DETECTED'
#     EV_MOTION_OFF = 'EV_MOTION_OFF'
#     # fires when alarm on a google home device
#     EV_ALARM_CLOCK_ALARM = 'EV_ALARM_CLOCK_ALARM'

#     # Commands
#     # play a program with a specific program id (see sr.se api for details)
#     CMD_SR_PLAY_PROGRAM = 'CMD_SR_PLAY_PROGRAM'
#     # send notification
#     CMD_NOTIFY = 'CMD_NOTIFY'
#     # send notification with greeting
#     CMD_NOTIFY_GREET = 'CMD_NOTIFY_GREET'
#     # turn on ambient lights
#     CMD_AMBIENT_LIGHTS_ON = 'CMD_AMBIENT_LIGHTS_ON'
#     # turn off ambient lights
#     CMD_AMBIENT_LIGHTS_OFF = 'CMD_AMBIENT_LIGTS_OFF'


class HouseModes(Enum):
    morning = 'Morning'
    day = 'Day'
    evening = 'Evening'
    night = 'Night'