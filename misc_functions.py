# ----- MISC FUNCTIONS -----

def get_adj_spaces(space):
    adj_up = {'x': space['x'], 'y': space['y'] + 1}
    adj_down = {'x': space['x'], 'y': space['y'] - 1}
    adj_left = {'x': space['x'] - 1, 'y': space['y']}
    adj_right = {'x': space['x'] + 1, 'y': space['y']}

    adj_spaces = {"up": adj_up, "down": adj_down, "left": adj_left, "right": adj_right}

    return adj_spaces


