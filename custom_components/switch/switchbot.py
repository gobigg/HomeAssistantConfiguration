import binascii
import bluepy
import logging
import time
import voluptuous as vol

from bluepy.btle import Peripheral

import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import SwitchDevice, PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_MAC


REQUIREMENTS = ['bluepy==1.2.0']

_LOGGER = logging.getLogger(__name__)

CHARS = 'cba20002-224d-11e6-9fb8-0002a5d5c51b'
DEFAULT_NAME = 'Switchbot'
ON_KEY = '570101'
OFF_KEY = '570102'
PRESS_KEY = '570100'
UUID = 'cba20d00-224d-11e6-9fb8-0002a5d5c51b'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_MAC): cv.string,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None) -> None:
    """Perform the setup for SwitchBot devices."""
    name = config.get(CONF_NAME)
    mac_addr = config.get(CONF_MAC)
    add_devices([SwitchBot(mac_addr, name)], True)

class SwitchBot(SwitchDevice):
    """Representation of a SwitchBot."""
    def __init__(self, mac, name) -> None:
        self._name = name
        self._mac = mac
        self._state = False

    def turn_on(self, **kwargs) -> None:
        """Turn device on."""
        for connection in range(1,6):
            try:
                self._device = Peripheral(self._mac, bluepy.btle.ADDR_TYPE_RANDOM)
            except:
                _LOGGER.error("Connection attempt failed after %s tries" % connection)
                time.sleep(10)
                continue
            break
        else:
            _LOGGER.error("Connection failed after max attempts")

        try:
            hand_service = self._device.getServiceByUUID(UUID)
            hand = hand_service.getCharacteristics(CHARS)[0]
            hand.write(binascii.a2b_hex(ON_KEY))
            self._device.disconnect()
            self._state = True
        except:
            _LOGGER.error("Cannot connect to %s" % self._name)

    def turn_off(self, **kwargs) -> None:
        """Turn device off."""
        for connection in range(1,6):
            try:
                self._device = Peripheral(self._mac, bluepy.btle.ADDR_TYPE_RANDOM)
            except:
                _LOGGER.error("Connection attempt failed after %s tries" % connection)
                time.sleep(30)
                continue
            break
        else:
            _LOGGER.error("Connection failed after max attempts")

        try:
            hand_service = self._device.getServiceByUUID(UUID)
            hand = hand_service.getCharacteristics(CHARS)[0]
            hand.write(binascii.a2b_hex(OFF_KEY))
            self._device.disconnect()
            self._state = False
        except:
            _LOGGER.error("Cannot connect to %s" % self._name)

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return self._state

    @property
    def name(self) -> str:
        """Return the name of the switch."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return a unique, HASS-friendly identifier for this entity."""
        return self._mac