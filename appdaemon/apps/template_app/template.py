from base import Base
import appdaemon.plugins.hass.hassapi as hass
import globals
from globals import HouseModes, PEOPLE
import datetime
from datetime import timedelta, date

class Template(Base):
    
    def initialize(self) -> None:
        """Initialize."""
        super().initialize()
