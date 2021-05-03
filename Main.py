def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    steps = params['steps']
    progress = params['progress']
    
    TOTAL_NUM_STEPS = 300
    reward = 0
    
    # Calculate 3 markers that are at varying distances away from the center line

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    marker_4 = 0.75 * track_width

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 50) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 50 :
        reward += 5.0
    if distance_from_center <= marker_1:
        reward += 1.0    
    elif distance_from_center <= marker_2:
        reward += 0.5
    elif distance_from_center <= marker_3:
        reward += 0.1
    elif distance_from_center <= marker_4:
        reward += -0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track


    return float(reward)