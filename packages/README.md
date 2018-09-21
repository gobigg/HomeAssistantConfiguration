# Packages
## I'm currently moving a lot of my automations to appdaemon. Packages will be left here for now with moved functionality commented out.

#### air_cleaner
Using a Broadlink RM3 turn on and off Air cleaner quiet mode.

#### alarm
Using Home Assistants Alarm Control Panel automatically arming and disarming on presence etc.

#### alarm_clock
Alarm clock with sensors and automation. Right now not using as a normal alarm clock, just automation trigger. Using Ios app and actionable notifications to let Hass know I'm up.

#### bathroom_fan
Using [PyCalima](https://github.com/PatrickE94/pycalima) command line sensor to get values from my bathroom fan. Currently not in use.

#### batteries
View and groups for batteries.

#### battery_alert
Package for dynamic creation of sensors for all entities with battery attributes, and notifications.

#### bedroom_lights
Controls bedroom lights with a Xiaomi switch.

#### camera_fireplace
Camera configuration and video notification if temperature seems to high in livingroom.

#### cats
Package for things concering the cats. Litterbox automations in separate package. More to come!

#### cleaning_day
Turns off certain behaviour that's not wanted when the cleaners are here and turning on all lights.

#### cleaning_time
Scripts to turn all lights on full for cleaning, putting on some cleaning music (upbeat playlist from Spotify playing on Sonos) and then when done cleaning dim the lights and turn some off again.

#### doors
Template sensors for door sensors and alerts when doors are left open.

#### ebike_charging_station
Reminder to charge my e-bike battery.

#### flood_sensors
Template sensors for flood sensors and alert for when they detect water leak.

#### floorlamp
Control the floorlamp with a Xiaomi switch. Toggle for both lights and dimmer for uplight.

#### goodnight
Script that can be called with Siri or Alexa to get ready for bed. Also playing some with trying to detect when we go to bed by tracking when our phones are charging, not working 100 %.

#### guest_mode
Boolean for setting the house in guest mode. Used to override automations. Turns on automatically when a friend connects to our wifi.

#### hallway_light
Control the uplight with a Xiaomi switch. Toggle light and toggle full and lower brightness. Long click press used for mailbox (see mailbox package).

#### homekit_specific
The native homekit component can't handle media players yet.

#### house
Things having to do with the whole house, more or less.

#### internet_monitor
Speedtests and router status.

#### laundry_dryer
Basically the same as laundry_washing_machine, see below.

#### laundry_outdoor
Keeping track of if there is laundry hanging to dry outdoor (on balcony) manually by pressing a switch. Notifications if there is a probability it's going to rain and laundry is hanging outdoor and if the laundry has hung outdoors for 12 hours (probably dry by then).

#### laundry_washing_machine
Sensor and input_select for washing machine (with the help of Fibaro wall plug). Automations for checking what state the washing machine is in and sending notifications and turning a light red (red light temporarely turned off) when it's done, but only under certain circumstances (time and presence). Using actionable notifications for ios.

#### lights_at_dark
Automations for turning on certain lights based on sunset, and turn them off again at night.

#### lights_at_presence
Automations for turning on certain lights if we come home during the night and then turning the Outdoor lights off again after ten minutes. Turn certain ceiling lights on if we come home based on sunset (it's nice to come home to a little bit of light during the winter especially).

#### lights_in_morning
Automations for turning certain lights on at 06.40 during the work week and turn them off again at sunrise.

#### lights
Script for movie time called by Alexa or Siri. Also using a custom state card with tiles (link in main readme) for controlling some scripts for lights. Generic light groups.

#### litterbox_downstairs and litterbox_upstairs
Help determine if the litterboxes need cleaning, send notifications and keeping track of visits to litterboxes. You can read about it [at the forums](https://community.home-assistant.io/t/smart-litter-box-or-smart-cats/27646) or [in swedish](https://www.automatiserar.se/tavlingsbidrag-smarta-kattlador/). Some changes made since both of these were written.

#### mailbox
Using two Xiaomi door/window sensors sending notifications when we get mail or packages in mailbox. Switch for resetting, delay so that I can press first, then get the mail, if on my way out.

#### miflora
Setup for my plant monitors.

#### motion_sensors
Template sensors for pirs.

#### presence_detection
Combining device_trackers to determine presence. Combined with a python script to update a custom device_tracker from latest update.

#### ring_doorbell
Flash lights when someone rings the doorbell using a python script to flash the lights and then return to previous state and brightness. Also turn the Outdoor front light and hallway window light to 100 % on ding or motion. Plus some other config for the Ring Doorbell.

#### roomba
Using a Broadlink RM3 to turn on, off and dock the Roomba robot vacuum. I use a Xiaomi door sensor to determine if the Roomba is docked. Using actionable notifications for ios to ask if the Roomba should vacuum when everyone is away.

#### smoke_alarm
Xiaomi Honeywell smoke alarms, sends notifications when (if) they go off.

#### stairs_lights
Mqtt light config for stairs lights (MiLight via mqtt).

#### stefan_radiator
Using a custom component I use a Switchbot to manually turn on my husbands radiator. The action happens on the slave hass on rpi3, since ble on Nuc with hass.io...

#### summary
Currently not in use, but I plan to implement soon. Link to summary card in the package.

#### svtplay
Using custom component for playing web tv on chromecast. Currently only using it to put the morning news on our NVidia Shield, but could do more.

#### system_info
Template sensors (with custom icons) to track states of the devices on our network. Automations for notifying when some of the more critical ones have been offline for more then five minutes. I'm using the nmap component to track the devices.
Groups for system information, internet status and network devices. Automations for when critical devices go offline.

#### system_monitor_hass
Automations for things that happens on start and stop of hass. Some sensors to keep track of my RPi3 slave Hass instance, other processes and speedtesting our internet.

#### temp_light_humidity
Graphs and groups for temperature, humidity and light sensors.

#### test_package
Package for...testing new stuff. (Commented out when not testing)

#### time_day
Things that has to do with time and time of day. Mostly for use in other automations.

#### upstairs_bathroom
Alert when forgetting to close bathroom cabinet.

#### vacation_mode
For running automations when we are on holiday.

#### walk_in_closet_lights
Exactly what it sounds like.

#### weather
Weather sensors and groups.

#### windows
Same as doors but for windows.

#### workday
Workday sensor, for use in automations. I have changed in the python file so that it takes swedish holidays instead of danish.