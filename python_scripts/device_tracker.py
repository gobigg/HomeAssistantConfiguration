# Get Data from Automation Trigger
triggeredEntity = data.get('entity_id')
metatrackerName = "device_tracker." + data.get('meta_entity')

# Get new state
newState = hass.states.get(triggeredEntity)
newStatus = newState.state

stefan = hass.states.get('device_tracker.stefan')
isabella = hass.states.get('device_tracker.isabella')

hass.states.set(metatrackerName, newStatus, {
    'friendly_name' : data.get('meta_entity')
})

# groupState = hass.states.get('group.persons')

# if stefan.state == 'Away' or stefan.state == 'Extended Away' or stefan.state == 'Just Left' and isabella.state == 'Away' or isabella.state == 'Extended Away' or isabella.state == 'Just Left':
#     hass.states.set('group.persons', 'not_home')
# else:
#     hass.states.set('group.persons', 'home')
# if groupState.state == 'not_home' or groupState.state == 'unknown':
#     if newStatus == 'Just Arrived':
#         hass.states.set('group.persons', newStatus)
