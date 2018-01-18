"""
Switch bot
"""
import asyncio
import logging
import voluptuous as vol

from homeassistant.util import convert
from homeassistant.components.switch import (SwitchDevice)
from homeassistant.const import (STATE_OFF, STATE_ON, CONF_NAME, CONF_SWITCHES)

import binascii
from bluepy.btle import Peripheral

import homeassistant.helpers.config_validation as cv

""" key's expected from user configuration"""
CONF_NAME = 'name'
CONF_MAC = 'mac'

DOMAIN = 'switchbot'
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
      vol.Required(CONF_MAC): cv.string,
    })
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Find and return Sensibo data"""
    my_name = config.get(CONF_NAME, 'switchbot')    
    my_mac = config.get(CONF_MAC)
    add_devices([SwitchBot(my_name, my_mac)])
    _LOGGER.info("Tried to setup SWITCH BOT.")

class SwitchBot(SwitchDevice):
    """Representation of a Switch Bot."""

    def __init__(self, my_name, my_mac):
        _LOGGER.info("Initialized Switch Bot SWITCH %s", my_name)
        self._name = my_name
        self._mac = my_mac
        self._state = False

    def turn_on(self, **kwargs):
        """Turn device on."""
        _LOGGER.debug("Update Switch Bot SWITCH to on")

        p = Peripheral(self._mac, "random")
        hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
        hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
        hand.write(binascii.a2b_hex("570101"))
        self._state = 'on'
        self.hass.states.set('sensor.' + self._name, 'on')

    def turn_off(self, **kwargs):
        """Turn device off."""
        _LOGGER.debug("Update Switch Bot SWITCH to off")

        p = Peripheral(self._mac, "random")
        hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
        hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
        hand.write(binascii.a2b_hex("570102"))
        self._state = 'off'
        self.hass.states.set('sensor.' + self._name, 'off')

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._state
    @property
    def name(self):
        """Return the name of the switch."""
        return self._name