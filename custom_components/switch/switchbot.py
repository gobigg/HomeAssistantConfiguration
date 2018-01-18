"""
Switch bot
"""
import logging
import voluptuous as vol

from homeassistant.util import convert
from homeassistant.components.switch import (SwitchDevice)
from homeassistant.const import (STATE_OFF, STATE_ON, CONF_NAME, CONF_SWITCHES)

import binascii
from bluepy.btle import Peripheral

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'switchbot'
""" key's expected from user configuration"""
CONF_NAME = 'name'
CONF_MAC = 'mac'

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Find and return Sensibo data"""
    my_name = config.get(CONF_NAME)    
    my_mac = config.get(CONF_MAC)
    add_devices([SwitchBot(my_name, my_mac)])
    _LOGGER.info("Tried to setup SWITCH BOT.")

class SwitchBot(SwitchDevice):
    """Representation of a Switch Bot."""

    def __init__(self, name, given_api_key):
        _LOGGER.info("Initialized Switch Bot SWITCH %s", name)
        self._name = name
        self._mac = given_api_key
        self._state = False
        # self.update()

    def turn_on(self, **kwargs):
        """Turn device on."""
        _LOGGER.debug("Update Switch Bot SWITCH to on")

        p = Peripheral(self._mac, "random")
        hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
        hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
        hand.write(binascii.a2b_hex("570101"))
        hass.states.set('sensor.stefan_radiator', 'on')

    def turn_off(self, **kwargs):
        """Turn device off."""
        _LOGGER.debug("Update Switch Bot SWITCH to off")

        p = Peripheral(self._mac, "random")
        hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
        hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
        hand.write(binascii.a2b_hex("570102"))
        hass.states.set('sensor.' + entity_id, 'off')

    # def update(self):
    #     _LOGGER.debug("Checking Sensibo SWITCH stats for  %s", self._name)
    #     client = SensiboClientAPI(self._givent_api_key)
    #     devices = client.devices()
    #     uid = devices[self._name]
    #     _LOGGER.debug("Sensibo uid =%s", uid)
    #     """Get the latest settings from the thermostat."""
    #     current_settings = client.pod_ac_state(uid)
    #     self._state = current_settings['on']