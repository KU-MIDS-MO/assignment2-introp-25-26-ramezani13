def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1

    if seconds == 0:
        return {}

    result = {}
    units = [3600, 60, 1]

    i = 0
    while i < len(units):
        unit = units[i]
        count = seconds // unit
        if count > 0:
            result[unit] = count
            seconds = seconds % unit
        i = i + 1
    return result
