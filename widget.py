import psutil
import requests
import rumps


def get_price(coin_type: str = 'BTC-INR'):
    """

    :param coin_type:
    :return:
    """
    response = requests.get(f'https://api.coinbase.com/v2/prices/{coin_type}/buy')
    if response.status_code == 200:
        body = response.json()['data']
        return "{}: {} {}".format(body['base'], body['amount'], body['currency'])
    else:
        return '{}: N/A'.format(coin_type)


def convert_value(value):
    """

    :param value:
    :return:
    """
    # Conversion to DB
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


def convert(val, divisor):
    """

    :param val:
    :param divisor:
    :return:
    """
    return round(val / divisor, 2)


def get_memory():
    """

    :return:
    """
    mem_usage = psutil.virtual_memory()
    available, available_unit = convert_value(mem_usage.used)
    total, total_unit = convert_value(mem_usage.total)
    pct = round(mem_usage.percent, 2)
    message = "{0}{1}/{2}{3} [{4}%]".format(available, available_unit, total, total_unit, pct)
    return message


class BatteryIndicator(rumps.App):
    def __init__(self, *args, **kwargs):
        super(BatteryIndicator, self).__init__(*args, **kwargs)

    @rumps.timer(2.5)
    def update(self, _):
        """

        :param _:
        :return:
        """
        self.title = get_memory()


if __name__ == "__main__":
    bi = BatteryIndicator(name='Currency Indicator')
    bi.run()
