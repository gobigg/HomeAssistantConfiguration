# Create placeholder device_tracker.meta entities at startup
hass.states.set('device_tracker.isabella', 'unknown', {
    'friendly_name': 'Isabella',
    'last_update_source': 'placeholder'
})

hass.states.set('device_tracker.stefan', 'unknown', {
    'friendly_name': 'Stefan',
    'last_update_source': 'placeholder'
})