# from base import Base
# from globals import PEOPLE#, house_modes
# import globals
# import datetime
# from datetime import timedelta, datetime
# import json

# class Doors(Base):

#     def initialize(self) -> None:
#         """Initialize."""
#         super().initialize()
#         self._tts_device = "media_player.sonos"
#         self.listen_state(self.door_open, "sensor.yard_door", new = "Open")

#     def door_open(self, entity, attribute, new, old, kwargs):
#         if get_state("sensor.presence_isa") == "Home" and :

#             self.tts_manager.set_volume_level('0.2', media_player=self._tts_device)
#             self.tts_manager.speak("Door opened", media_player = self._tts_device)