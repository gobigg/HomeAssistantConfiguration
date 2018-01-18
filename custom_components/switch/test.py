# Activate switchbot by python with bluepy on Raspberry Pi
# https://github.com/IanHarvey/bluepy
# 
# Switchbot's API is taken from this
# https://github.com/OpenWonderLabs/python-host

import binascii
from bluepy.btle import Peripheral

entity_id = data.get('entity_id')
action = data.get('action')

# find your switchbot address by
# pi@raspberry:~ $ sudo hcitool lescan
# replace "ff:..:ff"

# if entity_id == "stefan_radiator":
#     switchbot = "EA:E1:11:E2:B1:77"

p = Peripheral("EA:E1:11:E2:B1:77", "random")
hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]

if action == 'turn_on':
    hand.write(binascii.a2b_hex("570101"))
    hass.states.set('sensor.stefan_radiator', 'on')

elif action == 'turn_off':
    hand.write(binascii.a2b_hex("570102"))
    hass.states.set('sensor.' + entity_id, 'off')
    
elif action == 'press':
    hand.write(binascii.a2b_hex("570100"))

else:
    hass.states.set('sensor.' + entity_id , 'unknown')

p.disconnect()



# EA:E1:11:E2:B1:77 (unknown) !!