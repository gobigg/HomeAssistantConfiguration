# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')

# Get new state
newState = hass.states.get(triggeredEntity)
newStatus = newState.state

stefan = hass.states.get('device_tracker.stefan')
isabella = hass.states.get('device_tracker.isabella')


if metatrackerName == 'device_tracker.Stefan':
    picture = '/local/Stefan.jpg'
elif metatrackerName == 'device_tracker.Isabella':
    picture = '/local/Isa.jpg'  

hass.states.set(metatrackerName, newStatus, {
    'friendly_name' : data.get('meta_entity'),
    'entity_picture' : picture
})