def round_answer(val):
    """
    Rounds temperatures to the nearest degree
    :param val: Number to be rounded
    :return: Number rounded to the nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature in °F to be converted into °C
    :return: Converted temperature in °C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_answer(answer)


def to_fahrenheit(to_convert):
    """
    Converts from °F to °C
    :param to_convert: Temperature in °F to be converted into °C
    :return: Converted temperature in °C
    """
    answer = (to_convert * 9) / 5 + 32
    return round_answer(answer)

