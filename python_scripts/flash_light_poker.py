entity_id = 'light.floorlamp_uplight'
light = hass.states.get(entity_id)

original_state = light.state

hass.services.call('light', 'turn_off', {'entity_id': 'light.dining_area_ceiling_light_level'})
time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': entity_id})
time.sleep(1)
hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': '255', 'color_name': 'red'})
time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': entity_id})
time.sleep(1)
hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': '255', 'color_name': 'red'})
time.sleep(1)
hass.services.call('light', 'turn_off', {'entity_id': entity_id})
time.sleep(1)
hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': '255', 'color_name': 'red'})
time.sleep(1)

hass.services.call('light', 'turn_on', {'entity_id': entity_id, 'brightness': 100, 'kelvin': '3000'})
hass.services.call('light', 'turn_on', {'entity_id': 'light.dining_area_ceiling_light_level', 'brightness': 100})