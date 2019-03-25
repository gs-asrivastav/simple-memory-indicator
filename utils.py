def convert(val, divisor):
    """

    :param val:
    :param divisor:
    :return:
    """
    return round(val / divisor, 2)


def convert_value(value):
    """

    :param value:
    :return:
    """
    converted = value // (1024 ** 3)
    if converted is not 0:
        return convert(value, 1024 ** 3), 'GB'

    converted = value // (1024 ** 2)
    if converted is not 0:
        return convert(value, 1024 ** 2), 'MB'

    converted = value // 1024
    if converted is not 0:
        return convert(value, 1024), 'KB'

    return convert(value, 1), 'B'
