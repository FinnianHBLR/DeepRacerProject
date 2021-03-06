def reward_function(params):

    # Inputs
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    progress = params['progress']
    
    # Define Other Parameters
    TOTAL_NUM_STEPS = 300
    reward = 0

    # Calculate 4 markers that are at varying distances away from the center line

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    # Marker 4 for edge
    marker_4 = 0.75 * track_width

    # Give additional reward if the car pass every 50 steps faster than expected
    if (steps % 50) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 50 :
        reward += 5.0
    if distance_from_center <= marker_1:
        reward += 1.0    
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    elif distance_from_center <= marker_4:
        reward += -2
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Could make it get more reward on completion
    return float(reward)