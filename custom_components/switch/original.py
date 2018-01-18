# Activate switchbot by python with bluepy on Raspberry Pi
# https://github.com/IanHarvey/bluepy
# 
# Switchbot's API is taken from this
# https://github.com/OpenWonderLabs/python-host

import binascii
from bluepy.btle import Peripheral

# find your switchbot address by
# pi@raspberry:~ $ sudo hcitool lescan
# replace "ff:..:ff"
p = Peripheral("ff:ff:ff:ff:ff:ff", "random")
hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
hand.write(binascii.a2b_hex("570100"))
p.disconnect()