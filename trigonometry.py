def sin(angle_in_radians):
    return angle_in_radians - (angle_in_radians ** 3) / 6 + (angle_in_radians ** 5) / 120

def cos(angle_in_radians):
    return 1 - (angle_in_radians ** 2) / 2 + (angle_in_radians ** 4) / 24

def tan(angle_in_radians):
    return sin(angle_in_radians) / cos(angle_in_radians)
