# My Home Assistant Configuration
I'm often behind on updating the readme. Ask me about anything!
My configuration is broken down into [packages](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/README.md), sort of mini configuration-files. This makes it easy to see everything pertaining to a specific automation or implementation.

### Running Hass.io on an Intel Nuc with Ubuntu Server, in docker.
* Running a slave instance of Home Assistant on a Raspberry Pi 3 with a 16 gb memory card, since Hass.io can't use the Intel Nuc built in bluetooth (hoping for support soon!).
* Using native Homekit component to get support for Homekit and Siri.
* Using Home Assistant Cloud for Alexa.
#### Add-ons
* IDE
* MariaDB
* Mosquitto broker
* Samba share
* Terminal

## Hubs
* Zwave: Aeon Labs Z Wave Stick (GEN 5)
* Zigbee: Conbee (and Xiaomi hub, but am migrating to Conbee)
* Home made [MiLight hub](https://github.com/sidoh/esp8266_milight_hub)

## Ecosystem
#### Lights
* Hue
* Trådfri, dimmers and remotes via Hue bridge
* LIFX mini (only smart bulb that fits in my hallway window lamp)
* Milights
* Several Fibaro Dimmer 2

#### Phones, tablet and smart watches
* Ios-devices (iPhones, Apple watches, iPad mini)

#### Media
* Nvidia Shield TV (Android tv, media center)
* Plex Media Server
* Samsung Media system
* Two Samsung smart tv's
* Chromecast
* Sonos Play3
* Synology NAS

#### Security
* Yale Doorman
* Ring Doorbell 2 with one Chime (upstairs) and one Chime pro (downstairs)
* Sannce IP camera
* Neo Coolcam Flood sensor
* Neo Coolcam Door/Window sensors
* Neo Coolcam Pirs
* Xiaomi Flood sensor
* Xiaomi Door/Window sensors
* Xiaomi Pirs
* Sensative Strips Door sensor

#### Misc
* Xiaomi MiFloras (plant sensors)
* IRobot Roomba 880
* Electrolux Air Cleaner Z9124
* Withings WS-50 Smart Scale (currently not included)
* 3 Broadlink RM3 mini IR-blaster
* Xiaomi Switches (both round and square)
* Xiaomi Temperature and Humidity Sensors
* Fibaro Wall Plugs
* Pax Calima Bluetooth Bathroom Fan (currently not included)
* Switchbots
* and probably some more things I've forgotten to mention...

### Presence-detection
* Ios-app for Hass
* Nmap
* BT tracking
* Homekit
* Automations and python script to put information from above trackers together

## Automation hall of fame
### My favorite automations
* [Sending notifications when we get mail or packages in mailbox](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/mailbox.yaml)
* [Setting air cleaner in bedroom to quiet at 9 pm (before bedtime) and auto at 11 am (when we are sure to have gotten out of bed), using Broadlink RM3 mini ir blaster](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/air_cleaner.yaml)
* [Set light status on a few lights inside and Outdoor based on time of day,](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/lights_in_morning.yaml) [sun](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/lights_at_dark.yaml) [and when we come home](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/lights_at_presence.yaml)
* [Xiaomi switch by the bed toggles bedside lamp (single press), bedroom ceiling light (double press) or dim and brighten bedside lamp (long press)](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/bedroom_lights.yaml)
* [Not smart Roomba only vacuums when we're not home, starts using Broadlink RM3 mini ir blaster](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/roomba.yaml)
* [Monitoring and notifications when washer](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/laundry_washing_machine.yaml) [and dryer are done](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/laundry_dryer.yaml)
* [Say good morning to Siri and she turns on a couple of lights, and turns on the morning show on the living room tv if it's a work day](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/good_morning.yaml)
* [Say goodnight and all lights turn off, the bedside lamp and Xiaomi gw nightlight turns on, air cleaner gets quiet command and alarm goes to night mode](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/goodnight.yaml)
* [When someone uses the Ring Doorbell, flash lights in backyard and upstairs hallway](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/ring_doorbell.yaml)
* [Notifications for cleaning cat litterboxes](https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/packages/litterbox_upstairs.yaml)

## Future plans:
* Setting up a Magic mirror with information from Hass
* Setting up Floorplan on tablets

## Examples from my Lovelace gui
I have tried to make a gui that is mobile first, since that's how I most often look at it
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-home.png" alt="Home Assistant" width="200" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-home-info.png" alt="Home Assistant" width="200" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-lights.png" alt="Home Assistant" width="200" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-info.png" alt="Home Assistant" width="200" />

<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-home-web.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-home-info-web.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-lights-web.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/Lovelace-info-web.png" alt="Home Assistant" />


## Examples from my old gui
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/default_view.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/house_view.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/system_info.png" alt="Home Assistant" />
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/alarmclock.png" alt="Home Assistant" />

Floorplan gif-demo:
<img src="https://github.com/isabellaalstrom/HomeAssistantConfiguration/blob/master/Images/floorplangitgif.gif" alt="Home Assistant" />

## Recommended links
* [Hassbian](https://home-assistant.io/docs/installation/hassbian/)
* [How to backup your config on Github](https://home-assistant.io/docs/ecosystem/backup/backup_github/)
* [Homebridge](https://github.com/nfarina/homebridge) and [Homebridge for Home assistant](https://github.com/home-assistant/homebridge-homeassistant)
* [Backup your sd card with rpi-clone - in swedish](https://snillevilla.se/automatisk-sakerhetskopiering-av-raspberry-pi-minneskort/)
* [Custom_ui - for sliders, latest update, locks on switches etc.](https://github.com/andrey-git/home-assistant-custom-ui)
* [Tiles for Home Assistant - custom state card](https://github.com/c727/home-assistant-tiles)
* [Floorplan](https://github.com/pkozul/ha-floorplan)